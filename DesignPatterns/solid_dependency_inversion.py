class MySQLDatabase:
    def connect(self):
        print("connecting to mySqldatabase")
class Client1:
    def __init__(self):
        self.db=MySQLDatabase()
    def connecting(self):
        self.db.connect()
c=Client1().connecting()


#######################################################
####Correct way to do this###################
from abc import ABC,abstractmethod
class Database(ABC):
    @abstractmethod
    def connect(self):pass
class MySqlDb(Database):
    def connect(self):
        print("connecting to mysql db")
class PostgressDb(Database):
    def connect(self):
        print("connecting to postgress db")
class Client:
    def __init__(self,db:Database):
        self.db=db
    def connecting(self):
        self.db.connect()
c=Client(PostgressDb())
c.connecting()
