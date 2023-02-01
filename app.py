from connectdb import DatabaseConnector, DBhelper

class UserSignup:

    def __init__(self):
        # database connection code
        self.db = DatabaseConnector()
        self.menu()
    

    def menu(self):
        print(self.db)

        """This method is takes input and call methods according"""
        user_input = input("""
        1. Enter 1 to register ?
        2. Enter to login ?
        3. Exit() from system ?

        """)
        
        if user_input == '1':
            # Calling register method
            self.register()
        
        elif(user_input == '2'):
            # Calling Login method 
            self.login()
        
        else:
            # We are exits from system
            pass
    
    def register(self):
        """This method is register/insert a new user to database"""
        pass

    def login(self):
        """This method  will use to login or will make a query to database and perform according"""
        pass


# user1 = UserSignup
# print(user1)

class Student:

    def __init__(self):
        
        # database connection
        self.db = DBhelper()

        self.menu()

    
    def menu(self):
        print('Optimising menu here')
        user_inputs = input("""
        1. Enter to register ?
        2. Enter to login ?
        3. Enter to Exit()

        """)
        if(user_inputs == '1'):
            self.register()
        
        elif(user_inputs == '2'):
            self.login()
        
        else:
            print('Thank You! System is Exit() Now!')
        
    def register(self):
        print('Welcome to registeration steps')

        name = input('Enter name here:  ')
        email = input('Enter email id: ')
        password = input('Enter password here: ')


        result = self.db.data_insertion(name=name, email=email, passwrod=password)
        print(result)
        
    
    def login(self):
        name = input('Enter your email id: ')
        password = input('Enter your password: ')
        records = self.db.search_user(email=name, password=password)
        print(records)
        

s1 = Student()
