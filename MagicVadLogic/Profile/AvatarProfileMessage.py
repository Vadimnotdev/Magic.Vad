from MagicVadTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from MagicVadLogic.Avatar.LogicClientAvatar import LogicClientAvatar
from MagicVadServer.Database.Databasemanager import *

class AvatarProfileMessage(PiranhaMessage):
    def __init__(self, database: DataBase):
        super().__init__(0)
        self.database = database
        self.snapshotChecksum = 0

    def getMessageType(self) -> int:
        return 24334

    def getServiceNodeType(self) -> int:
        return 9

    def encode(self):
        LogicClientAvatar(self.database).encode(self.stream)
