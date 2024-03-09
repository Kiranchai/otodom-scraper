import psycopg2

class DatabaseManager:
    def __init__(self,database, user, password, host='localhost', port=5432):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                database = self.database,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port          
            )
            print("Connected to the database")
        except psycopg2.DatabaseError as error:
             print("Database connection error: ", error)
             raise
        
    def disconnect(self):
         if self.connection is not None:
              self.connection.close()
              print("Database connection closed")
              self.connection = None

    def execute_query(self, query, parameters=None):
         if self.connection is None:
              raise ValueError("Database connection is not established")
         
         with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, parameters)
                self.connection.commit()
                print("Query executed succesfully")
            except psycopg2.Error as error:
                 self.connection.rollback()
                 print("Query execution error: ", error)
                 raise
            