import mysql.connector
import sys


class DbConnector:
    """This class will make connection with database and perform different kind operation on existing database.
       In this class we will create new table, data insertion, fetching records, updating and deleting records from database.
       Created by Krishna Yadav  At 20/12/2022

       If Have Any Sugeestions ?  Welcome For That email = krishnayadav14342@gmail.com
    """

    def __init__(self):
        """Making database connection"""
        # database connection here
        try: 
            # connecting database
            self.db = mysql.connector.connect(host='localhost',
                                    database='userdb',
                                    user='root',
                                    password = '',
                )
            
            # check db is connected or not
            if(self.db.is_connected()):

                # creating a cursor
                self.cursor = self.db.cursor()
            else:
                print('Datebase is not connected')

        except mysql.connector.Error as err:
            print(f'Database Connection Error: \n {err} ')
            sys.exit('Program Terminated! here have problem with db connection')
        
        else: # printed if no error from try block only
            print('\n Congrats! Database is succesfuly connected you ready go!\n') 

    def create_table(self):
        """To create new table in database with their set of attributes and data-type"""
        try: 
            self.cursor.execute("""
            CREATE table employees(id int auto_increment primary key, name varchar(255), department varchar(255))
            """)
        except mysql.connector.Error as err:
            print('\n Table is not create getting Error! \n', err)
        
        else: 
            print('\nCongrats! Table is  create getting \n')
   
    def insert_data(self,name:str, dep:str):
        """Data insertion in speccific table with values"""
        try: 
            self.cursor.execute(f"""
            insert into 'employeinfo'(name, department) values ('{name}', '{dep}')
            """)
            self.db.commit() # applying the changes

        except mysql.connector.Error as err:
            print('Error While Insertion: \n', err)
        else:
            print('\nData successfuly inserted! ')

    def make_querie(self,name:str, dep=str):
        """Read data/records from employeinfo table"""
        try: 

            # qeurie based on name
            # self.cursor.execute(f"""
            # SELECT * FROM employeinfo where department='{dep}'

            # """)
            
            # records based on name and dep with having same
            # self.cursor.execute(f"""
            # SELECT * FROM employeinfo where name='{name}' AND department='{dep}'
            # """)
            
            # fetching all records from database
            # self.cursor.execute(""" 
            # SELECT * FROM employeinfo
            # """)
            
            # fetching all value of specific column
            self.cursor.execute(""" 
            SELECT  department from employeinfo
            """)
            
            # to know distinct(unique) department from table(employeinfo)

            # self.cursor.execute("""
            # SELECT DISTINCT department from employeinfo
            # """)
            
            # adding some new columns to exesting table using alert command
            # self.cursor.execute("""
            # ALTER TABLE employeinfo ADD (salary int, email varchar(255))

            # """)
            # self.db.commit() # apply the changes at databse level



            records = self.cursor.fetchall()
            print('\n',records)
        except mysql.connector.Error as err:
            print(f'Getting Error while fetching the records\n class:{err} \nmessage {err._full_msg}  ')
    
    def update_records(self):
        'Update the existing records with new value!'
        try:
            # before updating records
            sql_select_qry = (""" SELECT * FROM employeinfo where id=2 """)
            self.cursor.execute(sql_select_qry)
            record = self.cursor.fetchone()
            print(record)

            sql_update_qry = (""" UPDATE employeinfo SET name='krishna2'   WHERE id=2""")
            self.cursor.execute(sql_update_qry)  # executing update query
            self.db.commit()
            print('\nUpdataion Done Successfuly!')

            self.cursor.execute(sql_select_qry)
            record = self.cursor.fetchone()
            print(record)


        
        except mysql.connector.Error as err:
            print('Error While Updation: \n',err)
        else:
            print('\nUpdataion Done Successfuly!')
    
    def update_multiple_row(self):
        """Updating multiple records in signle sql query: like all value of row or column """
        try:
            self.cursor.execute('SELECT  DISTINCT department FROM employeinfo')
            record = self.cursor.fetchall()
            print(record)
            # updating specific id number
            # self.cursor.execute(""" UPDATE employeinfo SET salary=salary + 15000  WHERE id=2 """)
            
            # updating with specifc departement
            # self.cursor.execute(""" UPDATE employeinfo SET salary=salary + 15000  WHERE department='Backend' """)

            sql_update_qry = (f""" UPDATE employeinfo SET salary=salary+7778 WHERE departement='Backend' """)
            self.cursor.executemany(sql_update_qry, seq_params=None)

            self.db.commit()

           
        except mysql.connector.Error as err:
            print('Error in multiple updation\n', err)
        else: 
            print('Multiple row are updated!')
    
    def delete_records(self):
        """This method will delete records from database using different ways 
           For example using id,departement, or other fields.
        """
        try:
            # sql query for delete specific record with id 
            delet_query = (" DELETE FROM employeinfo WHERE id = 2  ")

            # sql query to delete records of specific department as Mechanical
            delet_query = (""" DELETE FROM employeinfo WHERE department = 'Mechanical'  """)
            
            # delete emp using their name
            delete_with_name = (""" DELETE FROM employeinfo WHERE name='Aisha' """)
            
            # delete emp of specific email
            delete_with_email = (""" DELETE FROM employeinfo WHERE email='krishna123@gmail.com' """)
            
            # executing delete sql query here
            self.cursor.execute(delete_with_email)
            self.db.commit()

        except mysql.connector.Error as err:
            print('Error While deletion \n',err)
        
        else:
            print('Records Successfuly deleted!')

db1 = DbConnector() # object creation

db1.create_table() # create table in database
# db1.insert_data(name='Aman', dep='Mechanical')
# db1.make_querie(name='Aman', dep='Mechanical')
# db1.update_multiple_row()
# db1.delete_records()