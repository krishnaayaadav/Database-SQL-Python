import  mysql.connector
import sys
class DBConnector:

    def __init__(self):
        try:

            self.db = mysql.connector.connect(
                host = 'localhost',
                database = 'userdb',
                user='root',
                password = '',
            )

            if (self.db.is_connected()):
                print('Database is connected successfuly')

                # Making cursor here
                self.my_cursor = self.db.cursor()
            else:
                print('Database is not connected')
        except mysql.connector.Error as err:
            print(f'\n DB Error:\n {err}  ') 
            sys.exit('Database is not Connected! ')
    
    def search_records(self, name=None,password=None, email=None):
        try:
            # getting all records of users tables
            # self.my_cursor.execute(f""" SELECT * FROM `users` """)

            # reading one record only
            self.my_cursor.execute(f""" 
            SELECT * FROM users WHERE email LIKE '{email}' AND password LIKE '{password}' 

              """)
            records = self.my_cursor.fetchall()
            return records
        except mysql.connector.Error as err:
            print(f'Query DB Error: \n  {err}  ')
c1 = DBConnector()
print(c1.search_records(password='1234',name='krishna', email='krishna123@gmail.com'))