import mysql.connector
import mysql.connector.errors
import sys


class DatabaseConnector:

    def __init__(self):
        # using try except block to handle exception during db connection
        try: 
            # connecting our database at localhost/server
            self.connection = mysql.connector.connect(host='localhost',
                                                database='userdb',
                                                user='root',
                                                password=''
                                                )
            # checking weather database is connected or not
            if(self.connection.is_connected()): 
                print('\n server info: \n', self.connection.get_server_info())
                # Creating cursor to access db at serval times
                self.mycursor = self.connection.cursor()

                print(f'db cursor is: {self.mycursor} \n ')
                
                # executing cursor
                self.mycursor.execute()
                record = self.mycursor.fetchone()

                print(f'\nrecords are: {record} ')
                print('Database Connected Successfuly')

        except mysql.connector.Error as error: 
            print('Database connections Errors!\n',error)
        
  

class DBhelper:

    def __init__(self):
        try: 
            self.connection = mysql.connector.connect(host='localhost',
                                                    database ='userdb',
                                                    user = 'root',
                                                    password  = '')
            # if (self.connection.is_connected()):
            print('Databas is connected successfuly')

            self.mycursor = self.connection.cursor()

        except mysql.connector.Error as erors:
            print(f'\n Getting errors \n {erors} ')
            sys.exit('\nExecution Terminated!')
        
        finally: 
            pass
    
    def data_insertion(self, name, email, passwrod):
        try:
            self.mycursor.execute(f"""
            INSERT INTO `users`(`id`, `name`, `email`, `password`) VALUES (NULL, '{name}', '{email}', '{passwrod}')
            
            """)
            self.connection.commit()
            print('\nSuccessfuly Inserted')

        except mysql.connector.Error as error:
            print(f'Erorr during insertion\n {error} ')
            sys.exit('\n Execution Terminated')

    def search_user(self,email, password):
        try: 
            self.mycursor.execute(f"""
            SELECT * FROM users WHERE email LIKE '{email}' AND password LIKE '{password}' 
            """)
            records = self.mycursor.fetchone()
        except mysql.connector.Error as error:
            print(f'Getting some error during searching records\n {error} ')

