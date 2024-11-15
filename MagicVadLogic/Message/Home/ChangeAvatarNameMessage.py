from MagicVadTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from MagicVadServer.Database.Databasemanager import *
class ChangeAvatarNameMessage(PiranhaMessage):
    def __init__(self):
        super().__init__(0)
        self.removeAvatarName = True
        self.nameSetByUser = True
        self.avatarName = ""
    
    def decode(self):
        super().decode()
        self.avatarName = self.stream.readString()
        self.nameSetByUser = self.stream.readBoolean()

    def setAvatarName(self, avatarName: str):
        self.avatarName = avatarName

    def getAvatarName(self):
        return self.avatarName

    def getMessageType(self):
        return 10212
    
    def getServiceNodeType():
        return 9