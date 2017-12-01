# coding=utf-8
'''
CREATE TABLE Users (
    id INT(11) AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    username VARCHAR(255) NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    PRIMARY KEY(id)
);
'''



from clcrypto import password_hash
from dbconnection import DBconnection

db = DBconnection(user='root', password='coderslab', database='Workshop')
cnx = db.cnx
cursor = db.cursor

class User():
    __id = None
    username = None
    __hashed_password = None
    email = None

    def __init__(self):
        self.__id = -1
        self.username = ""
        self.email = ""
        self.__hashed_password = ""

    @property
    def id(self):
        return self.__id

    @property
    def hashed_password(self):
        return self.__hashed_password


    def set_password(self, password):
        self.__hashed_password = password_hash(password)

    def save_to_db(self, cursor):
        if self.__id == -1:
            sql = """INSERT INTO Users(username, email, hashed_password) VALUES ('{}', '{}', '{}')"""
            cursor.execute(sql.format(self.username, self.email, self.hashed_password))
            cnx.commit()
            self.__id = cursor.lastrowid
            return True
        else:
            sql = """UPDATE Users SET username='{}', email='{}', hashed_password='{}' WHERE id={}"""
            cursor.execute(sql.format(self.username, self.email, self.hashed_password, self.__id))
            cnx.commit()
            return True


    @staticmethod
    def load_user_by_username(cursor, username):
        sql = 'SELECT id, username, email, hashed_password FROM Users WHERE username="{}"'
        cursor.execute(sql.format(username))
        data = cursor.fetchone()
        if data is not None:
            loaded_user = User()
            loaded_user.__id = data[0]
            loaded_user.username = data[1]
            loaded_user.email = data[2]
            loaded_user.__hashed_password = data[3]
            return loaded_user
        else:
            return None

    @staticmethod
    def load_all_users(cursor):
        sql = 'SELECT id, username, email FROM Users'
        ret = []
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            loaded_user = User()
            loaded_user.__id = row[0]
            loaded_user.username = row[1]
            loaded_user.email = row[2]
            ret.append(loaded_user)
        return ret

    def delete(self, cursor, username):
        sql = 'DELETE FROM Users Where username="{}"'
        cursor.execute(sql.format(self.username))
        cnx.commit()
        self.__id = -1
        return True

    @staticmethod
    def validation(cursor, val, where=''):
        sql = 'SELECT {} FROM Users'.format(val)
        if where:
            sql += " WHERE {}".format(where)
        cursor.execute(sql)
        results = []
        result = cursor.fetchall()
        for usr in result:
            results.append(list(usr)[0]) # kombinowałem, żeby wydobyć z cursora listę stringów
        return results


# db = DBconnection(user='root', password='coderslab', database='Workshop')
# cnx = db.cnx
# cursor = db.cursor

# us = User()
# print(us.validation(cursor, 'username', where='id=2'))
#user_1 = User()
#
#
# user_1.username = 'Gosia'
# user_1.email = 'gosia@def.com'
# user_1.set_password('qwertytg')
# #print(user_1.__id)
# # print(user_1.hashed_password)
# user_1.save_to_db(cursor)

# user_2 = User()
#
# user_2.username = 'Gosia'
# user_2.email = 'def@def.com'
# user_2.set_password('abcdefg')
# print(user_2.hashed_password)
# user_2.save_to_db(cursor)

#test_user = User.load_user_by_username(cursor, 'user_1')
#print(test_user.id)
#print(test_user)

#test_user.delete(cursor)

#test_user.username = 'Malgorzata'
#test_user.save_to_db(cursor)

#u = User.load_all_users(cursor)
#print(u)

#u_1 = vars(u[0])
#print(u_1)

#cnx.close()