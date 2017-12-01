# coding=utf-8
import argparse

from clcrypto import check_password, password_hash
from user import User
from dbconnection import DBconnection

db = DBconnection(user='root', password='coderslab', database='Workshop')
cnx = db.cnx
cursor = db.cursor

def set_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', help="user's login")
    parser.add_argument('-p', '--password', help="user's password")
    parser.add_argument('-n', '--new_pass', help="user's new password")
    parser.add_argument('-l', '--list', action="store_true", help="lists all users")
    parser.add_argument('-d', '--delete', action="store_true", help="deletes user")
    parser.add_argument('-e', '--edit', action="store_true", help="edits user's data")
    args = parser.parse_args()
    return args

options = set_options()

if options.username and options.password:
        if options.edit:
            if not options.new_pass:
                raise Exception('No new password given')
            else:
                if options.username in User.validation(cursor, 'username'):
                    hashed = ''.join(
                        User.validation(cursor, 'hashed_password', where='username = "{}"'.format(options.username)))
                    if check_password(options.password, hashed) == True:
                        if len(options.new_pass) >= 8:
                            loaded_user = User.load_user_by_username(cursor, options.username)
                            loaded_user.set_password(options.new_pass)
                            loaded_user.save_to_db(cursor)
                            cnx.commit()
                        else:
                            raise Exception('New password is too short')
                    else:
                        raise Exception('Wrong password!')
                else:
                    raise Exception('such username does not exist!')
        elif options.delete:
            if options.username in User.validation(cursor, 'username'):
                hashed = ''.join(
                    User.validation(cursor, 'hashed_password', where='username = "{}"'.format(options.username)))
                if check_password(options.password, hashed) == True:
                    loaded_user = User.load_user_by_username(cursor, options.username)
                    loaded_user.delete(cursor, options.username)
                    cnx.commit()
                else:
                    raise Exception('Wrong password!')
            else:
                raise Exception('such username does not exist!')
        else:
            if options.username in User.validation(cursor, 'username'):
                raise Exception('Such user already exists')
            elif len(options.password) < 8:
                raise Exception('the password is too short!')
            else:
                new_user = User()
                new_user.username = options.username
                new_user.set_password(options.password)
                new_user.email = '{}@test.com'.format(options.username)

                new_user.save_to_db(cursor)
                cnx.commit() #Dlaczego nie wyłapuje commita z klasy?
if options.list:
    All_users = User.load_all_users(cursor)
    for usr in All_users:
        print(vars(usr))




cnx.close()




#Zakładamy funkcję dla obu programów?