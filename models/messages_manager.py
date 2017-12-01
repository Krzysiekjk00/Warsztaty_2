# coding=utf-8

import argparse

from clcrypto import check_password, password_hash
from Message import Message
from dbconnection import DBconnection
from user import User

db = DBconnection(user='root', password='coderslab', database='Workshop')
cnx = db.cnx
cursor = db.cursor

def set_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', help="user's login")
    parser.add_argument('-p', '--password', help="user's password")
    parser.add_argument('-l', '--list', action="store_true", help="lists all messages of user")
    parser.add_argument('-t', '--to', help="sets recipient")
    parser.add_argument('-s', '--send', '--send', help="sends a message")
    args = parser.parse_args()
    return args

options = set_options()

if options.username and options.password:
    if options.username in User.validation(cursor, 'username'):
        hashed = ''.join(
            User.validation(cursor, 'hashed_password', where='username = "{}"'.format(options.username)))
        if check_password(options.password, hashed) == True:
            if options.list:
                loaded_user = User.load_user_by_username(cursor, options.username)
                All_messages = Message.load_all_messages_for_user(cursor, loaded_user.id)
                for msg in All_messages:
                    print(vars(msg))
            elif options.send:
                if not options.to:
                    raise Exception('No recipient given!')
                else:
                    if options.to not in User.validation(cursor, 'username'):
                        raise Exception('Such recipient does not exist!')
                    else:
                        new_messsage = Message()
                        loaded_sender = User.load_user_by_username(cursor, options.username)
                        new_messsage.sender = loaded_sender.id
                        loaded_recipient = User.load_user_by_username(cursor, options.to)
                        new_messsage.recipient = loaded_recipient.id
                        new_messsage.content = options.send
                        new_messsage.save_message_to_db(cursor)
                        cnx.commit()
        else:
            raise Exception('Wrong password!')
    else:
        raise Exception('such username does not exist!')

