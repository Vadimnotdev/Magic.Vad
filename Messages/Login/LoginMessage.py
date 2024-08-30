from Messages.PiranhaMessage import PiranhaMessage
from Logic.LogicLong import LogicLong
class LoginMessage(PiranhaMessage):
    def __init__(self) -> None:
        super().__init__(0)
        self.AccountId: LogicLong = LogicLong()
        self.AndroidID = ""
        self.ClientMajorVersion = -1
        self.ClientBuild = -1
        self.PreferredLanguage = 0
        self.isAndroid = 0
        self.passToken = self.stream.readString()
    
    def getAndroidID(self):
        return self.AndroidID
    
    def getClientBuild(self):
        return self.ClientBuild
    
    def getClientMajorVersion(self):
        return self.ClientMajorVersion
    
    def getMessageType(self) -> int:
        return 10101
    
    def getPreferredLanguage(self):
        return self.PreferredLanguage
    
    def getServiceNodeType():
        return 1
    
    def isAndroid(self):
        return self.isAndroid

    
    def decode(self):
        super().decode()
        self.accountId = self.stream.readLong()
        self.passToken = self.stream.readString()
        self.ClientMajorVersion = self.stream.readInt()
        self.stream.readInt()
        self.ClientBuild = self.stream.readInt()
        self.ResourceSha = self.stream.readString()
        self.UDID = self.stream.readString()
        self.OpenUDID = self.stream.readString()
        self.MacAddress = self.stream.readString()
        self.MacAddress = self.stream.readString()