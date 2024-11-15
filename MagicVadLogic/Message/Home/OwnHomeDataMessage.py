from MagicVadTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from MagicVadLogic.Avatar.LogicClientAvatar import LogicClientAvatar
from MagicVadLogic.Home.LogicClientHome import LogicClientHome
from MagicVadServer.Database.Databasemanager import *
class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self, database: DataBase) -> None:
        super().__init__(0)
        self.database = database
        self.clientHome = LogicClientHome(database)
        self.clientAvatar = LogicClientAvatar(database)
    
    def getMessageType(self) -> int:
        return 24101
    
    def encode(self):
        super().encode()
        self.stream.writeInt(0)
        self.clientHome.encode(self.stream)
        self.clientAvatar.encode(self.stream)