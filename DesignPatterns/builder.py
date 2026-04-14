class Database:
    def __init__(self,builder:"Database.Builder"):
        self.host=builder.host
        self.port=builder.port
        self.username=builder.username
        self.password=builder.password
    def connect(self):
        print(f"database connected to {self.host} with port {self.port} with username {self.username}")
    @staticmethod
    def builder():
        return Database.Builder()
    class Builder:
        def __init__(self):
            self.host=None
            self.port=None
            self.username=None
            self.password=None
        def set_host(self,host:str):
            self.host=host
            return self
        def set_port(self,port:int):
            self.port=port
            return self
        def set_username(self,username:str):
            self.username=username
            return self
        def set_password(self,password:str):
            self.password=password
            return self
        def _validate(self):
            if self.host is None:
                raise ValueError("host name needed")
        def build(self):
            self._validate()
            return Database(self)
if __name__=="__main__":
    config=(Database.builder()
            .set_host("prod")
            .set_port(5555)
            .set_username("ram")
            .set_password("9ys9aud")
            .build())
    print(config.connect())