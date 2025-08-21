class Database:
    objects = {}   # to keep one object per subclass, server & port
    
    # Task-4: Dunder for reusing existing connection instead of creating a new one
    def __new__(cls, server, port):
        key = (cls, server, port)   # unique key for each connection

        if key not in cls.objects:
            object = super().__new__(cls)
            cls.objects[key] = object
            print("Connection success!")
        else:
            print("Connection Already Exists. Reusing.....")
        return cls.objects[key]
    
    # Task-2: Base class will automatically store Server & Port While Creating New connection
    def __init__(self, server, port):
        self.server = server
        self.port = port
       
    # Task-3: Method Overriding Polymorphism
    def connect(self):
        print(f"Connecting to Base database...")

# Task-1: Separate classes for Orders, Cache & Analytics Database

class OrdersDatabase(Database):
    def connect(self):
        print(f"Connecting to Orders database...")


class CacheDatabase(Database):
    def connect(self):
        print(f"Connecting to Cache database...")


class AnalyticsDatabase(Database):
    def connect(self):
        print(f"Connecting to Analytics database...")
        
        
# Testing: 

db1 = OrdersDatabase("127.0.0.1", 5432)  # Connection success!
db1.connect()  # Connecting to Orders database...
db2 = OrdersDatabase("127.0.0.1", 5432)  # Connection Already Exists. Reusing.....

db3 = CacheDatabase("127.0.0.1", 5432)  # Connection success!
db4 = CacheDatabase("127.0.0.1", 5432)  # Connection Already Exists. Reusing.....

db5 = AnalyticsDatabase("127.0.0.1", 5432)  # Connection success!
db6 = AnalyticsDatabase("127.0.0.1", 5432)  # Connection Already Exists. Reusing.....



  
