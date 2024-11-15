from MagicVadTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from MagicVadTitan.Logic.Math.LogicLong import LogicLong
from MagicVadTitan.Logic.Message.PiranhaMessage import PiranhaMessage


class LoginMessage(PiranhaMessage):
    def __init__(self):
        super().__init__(0)
        self.avatarHighId = 0
        self.avatarLowId = 0
        self.passToken = ""
        self.ClientMajorVersion = 0
        self.ClientBuild = 0
        self.ResourceSha = ""
        self.UDID = ""
        self.OpenUDID = ""
        self.MacAddress = ""
        self.avatarId = LogicLong(self.avatarHighId, self.avatarLowId)
    
    def getMessageType(self) -> int:
        return 10101
    
    def decode(self):
        super().decode()
        self.avatarHighId = self.stream.readInt()
        self.avatarLowId = self.stream.readInt()
        self.passToken = self.stream.readString()
        self.ClientMajorVersion = self.stream.readInt()
        self.stream.readInt()
        self.ClientBuild = self.stream.readInt()
        self.ResourceSha = self.stream.readString()
        self.UDID = self.stream.readString()
        self.OpenUDID = self.stream.readString()
        self.MacAddress = self.stream.readString()
        self.MacAddress = self.stream.readString()
        self.avatarId = LogicLong(self.avatarHighId, self.avatarLowId)
