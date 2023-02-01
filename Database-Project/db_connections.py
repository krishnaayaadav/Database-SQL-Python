import mysql.connector 
import sys

class Database:
    """This will cover all functionality of database like create database/tables,
        records insertion,updation or deletion and fetching data in different ways.
        Created by Krishna Yadav at 21/11/2022
    """

    def __init__(self):
        """Making databas connections and cursor object creation here"""

        try: 
            self.connection = mysql.connector.connect(host='localhost'
                                                         ,database='EmployeeDB',
                                                          user='root',
                                                           password='')
            if self.connection.is_connected(): # checking if database is connected or not                                                           

                self.my_cursor = self.connection.cursor()  # Cursor object creation here

        except mysql.connector.Error as err:
            print('\nError while database connection \n', err) 
        
        else:
            print('\n Database is connected your ready to go')
    
    def  create_table(self):
        """Create Employee table with id as primary key, name,email,phone,department, salary"""
        try: 
            # Table creation sql query
            create_table_qry = (""" CREATE TABLE IF NOT EXISTS EMPLOYEES(
                emp_id int  AUTO_INCREMENT PRIMARY KEY,
                name varchar(230),
                email varchar(230) Not Null UNIQUE,
                phone varchar(23),
                department varchar(34),
                salary int Not Null
            ) """)

            self.my_cursor.execute(create_table_qry)
            self.connection.commit()

        except mysql.connector.Error as err:
            print('Error while table creation\n', err)
        else:
            print('\n Table successfuly created')
    
    def records_insertion(self, name:str,email:str,department:str, phone:str, salary:int):
        """This method will insert records in EMPLOYEES table above all fields are required!"""

        try:
            self.my_cursor.execute(f""" INSERT INTO EMPLOYEES(name,email,phone,department,salary) VALUES('{name}', '{email}', '{phone}', '{department}', {salary})""")
            self.connection.commit()
       
        except mysql.connector.Error as err: # error hanlding here
            print('Error While Data Insertion\n', err)
        
        else:
            print('Records Successfuly Inserted!')

    def alter_table(self):
        """This method will perform alter tables in terms of add new columns,
           drop columns, update or rename column name and their data types"""
        try:
            # Create table here of student
            create_table = (""" CREATE TABLE STUDENTS(
                StuName     VARCHAR(34),
                StuEmail    VARCHAR(34) NOT NULL UNIQUE,
                Stumarks    INTEGER NOT NULL,
                StuSection  VARCHAR(43)
                ) """)
           
            # add SINGLE new column to existing table
            add_new_column = (" ALTER TABLE STUDENTS ADD StuGrades VARCHAR(34) ")
            
            # Add multiple columns
            add_multiple_col = ("""
            ALTER TABLE STUDENTS
            ADD StuAddress VARCHAR(45),
            ADD StuAge     VARCHAR(51)
            """)
      
            # Modify column data-types 
            modify_column = (""" 
            ALTER TABLE STUDENTS
            MODIFY Stumarks INTEGER NULL,
            MODIFY StuAge   VARCHAR(34) 
            """)
            
            # change cmd is use change data-typ of columns as well as rename the columns also
            rename_column = ("""
            ALTER TABLE STUDENTS
            CHANGE StuEmail Email VARCHAR(34) NOT NULL UNIQUE
            """)

            # rename multiple columns
            rename_mul_columns = (""" 
            ALTER TABLE STUDENTS
            CHANGE StuName Name VARCHAR(45),
            CHANGE StuAge  Age INTEGER ,
            CHANGE StuSection Section VARCHAR(45)
            """)
            
            # drop single column from table
            drop_column = ("""
            ALTER TABLE STUDENTS
            DROP COLUMN Name
            """)
            
            # drop multiple columns
            drop_mul_col = ("""
            ALTER TABLE students
            DROP COLUMN StuMarks,
            DROP COLUMN StuGrades,
            DROP COLUMN StuAddress
            """)
           
            # Executing sql_query
            self.my_cursor.execute(drop_mul_col)
            self.connection.commit()

        except mysql.connector.Error as err:        # Exception handling here
            print('Error while table creation\n', err)
        else:
            print('Table is created successfuly\n')  # Success Message Display

d1 = Database()

# d1.create_table()
# d1.records_insertion(name='krana', email='karna@gmail.com', department='Front-End', phone='895', salary=64000)

d1.alter_table()
