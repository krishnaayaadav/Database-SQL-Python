
import mysql.connector
import sys
import time


class DBConnector:
    """This class will perform below operations :
    1 .database connection
    2. create table as employee( id not null auot_increment, salary, email, departement )
    3.insertion in database
    4.read data from database
    5.Update the data existing records with different ways

    Created by Krishna Yadav At 15/01/2020
    """
    
    def __init__(self):
        """This will establish database connection"""
        try:
            # making db connection
            self.db_connection = mysql.connector.connect(host='localhost', database='userdb', user='root', password='')
            
            # checking weather db is connected or not!
            if self.db_connection.is_connected():

                #  cursor object  here
                self.my_cursor = self.db_connection.cursor() 

        except mysql.connector.Error as err:
            print('Error While Database Connection!\n',err)   # displaying exception errors
            sys.exit('\nSorry! Database is Not Connected!')   # terminated all program
        else:
            print('\nDatabase is Connected You Are Ready Go..')
    
    def table_creation(self):
        """This will create table of employe"""
        try: 
            create_table_qry = (" CREATE TABLE EMP3(id int auto_increment primary key, name varchar(255), email varchar(255), department varchar(255))  ")
            drop_table = ("DROP TABLE emp2 ")
            self.my_cursor.execute(create_table_qry)
            self.db_connection.commit()
           
        except mysql.connector.Error as err:
            print('Error while table creation: \n',err)
        else:
            print('Table is created successfuly')
    
    def data_insertion(self,**kwargs ):
        """This will insert the data/records in given table from user with its data required"""
        try: 

            if( ('table' not in  kwargs.keys()) ): # checking if table name is not in dict than return them
                print('table is required')
                return

            
            tbl_name = kwargs['table'] # table name here
            
            keys = list(kwargs.keys())
            values =  list(kwargs.values())
            key_len = len(keys)

            st = ' """ '
            end = ' """ '

            insertion_qry = (f"""insert into {tbl_name}(""")
            key_end = ') values('
            val_end = ')'
            
            # adding all key to insertion query
            for i in range(0, key_len):
                if(keys[i] != 'table'):
                    if(i == key_len - 1):
                        insertion_qry += keys[i]
                    else:
                        insertion_qry = insertion_qry + keys[i] + ', '
            
            insertion_qry += key_end
            
            # adding all values
            for i in range(0, key_len):
                if(values[i] != tbl_name):
                    if(i == key_len -1):
                        insertion_qry += f'"{str(values[i])}"'
                    else:
                        insertion_qry  = insertion_qry + f'"{str(values[i])}"' + ', '
            
            insertion_qry += val_end

            print()
            print(insertion_qry)

            # insert query
            self.my_cursor.execute(insertion_qry)
            self.db_connection.commit()
        
        except mysql.connector.Error as err:
            print('Error while insertion\n', err)

        else:
            print('\n Data inserted successfuly')



con1 = DBConnector() # object creation here
# con1.table_creation()

con1.data_insertion(name='krishna', email='custom@gmail.com', table='users', password='cuspass12@' )


# keys = ''
# sql = ('INSERT INTO user(' )
# a = ') VALUE('
# a2 = ')'


# keys = list(datas.keys())
# key_l = len(keys)
# for i in range(0,key_l):
#     if(keys[i] != 'table'):
#         if(i == key_l-1):
#             sql = sql + keys[i]
#         else:
#             sql = sql + keys[i] + ','
#     else:
#         pass
# sql+= a


# table = datas['table']
# values = list(datas.values())
# val_ln = len(values)
# for i in range(0, val_ln):
#     if(values[i] !=table):
#         if(i == val_ln-1):
#             sql = sql + values[i]
#         else:
#             sql = sql + values[i] + ','

# sql += a2
# print(sql)
# # sql_qry = 
# print('keys are: ', (keys))




