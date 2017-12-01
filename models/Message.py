# coding=utf-8
'''
CREATE TABLE Messages (
    id INT AUTO_INCREMENT,
    sender INT NOT NULL,
    recipient INT NOT NULL,
    content TEXT,
    creation_date DATE,
    PRIMARY KEY(id),
    FOREIGN KEY(sender) REFERENCES Users(id),
    FOREIGN KEY(recipient) REFERENCES Users(id)
    );
'''
from dbconnection import DBconnection
from datetime import date

db = DBconnection(user='root', password='coderslab', database='Workshop')
cnx = db.cnx
cursor = db.cursor

class Message():
#usunąłem tu coś - zapamiętać

    def __init__(self):
        self.__id = -1
        self.sender = None
        self.recipient = None
        self.__content = ""
        self.creation_date = None

    @property
    def id(self):
        return self.__id


    @staticmethod
    def load_message_by_id(cursor, id):
        sql = 'SELECT * FROM Messages WHERE id={}'
        cursor.execute(sql.format(id))
        data = cursor.fetchone()
        if data is not None:
            loaded_message = Message()
            loaded_message.__id = data[0]
            loaded_message.sender = data[1]
            loaded_message.recipient = data[2]
            loaded_message.content = data[3]
            loaded_message.creation_date = data[4]
            return loaded_message
        else:
            return None


    @staticmethod
    def load_all_messages_for_user(cursor, recipient):
        sql = 'SELECT * FROM Messages WHERE recipient={} ORDER BY creation_date DESC'
        ret = []
        cursor.execute(sql.format(recipient))
        result = cursor.fetchall()
        for row in result:
            loaded_message = Message()
            loaded_message.__id = result[0]
            loaded_message.sender = result[1]
            loaded_message.recipient = result[2]
            loaded_message.content = result[3] #index error!
            loaded_message.creation_date = result[4]
            ret.append(loaded_message)
        return ret

    @staticmethod
    def load_all_messages(cursor):
        sql = 'SELECT * FROM Messages'
        ret = []
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            loaded_message = Message()
            loaded_message.__id = result[0]
            loaded_message.sender = result[1]
            loaded_message.recipient = result[2]
            loaded_message.content = result[3]
            loaded_message.creation_date = result[4]
            ret.append(loaded_message)
        return ret


    def save_message_to_db(self, cursor):
        sql = """INSERT INTO Messages(sender, recipient, content, creation_date) VALUES ({}, {}, '{}', '{}')"""
        cursor.execute(sql.format(self.sender, self.recipient, self.content, date.today()))
        cnx.commit()
        self.__id = cursor.lastrowid
        return True


# test = Message.load_all_messages_for_user(cursor, 14)
# print(vars(test[0]))