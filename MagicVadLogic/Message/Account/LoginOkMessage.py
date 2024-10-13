from MagicVadTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from MagicVadTitan.Logic.Math.LogicLong import LogicLong
class LoginOkMessage(PiranhaMessage):
    def __init__(self):
        super().__init__(0)
    
    def getMessageType(self) -> int:
        return 20104
    
    def encode(self):
        super().encode()

        self.stream.writeLong(LogicLong(1, 1)) # Account Id
        self.stream.writeLong(LogicLong(1, 1)) # Home Id
        self.stream.writeString("PassToken")
        self.stream.writeString("FacebookAppId")
        self.stream.writeString("GamecenterId")
        self.stream.writeInt(5) # ServerMajorVersion
        self.stream.writeInt(2) # ServerBuild
        self.stream.writeInt(4) # ContentVersion
        self.stream.writeString("dev") # ServerEnvironment
        self.stream.writeInt(1) # SessionCount
        self.stream.writeInt(1) # PlayTimeSeconds
        self.stream.writeInt(0) # DaysSinceStartedPlaying
        self.stream.writeString("FacebookAppId") # FacebookAppId
        self.stream.writeString("ServerTime") # ServerTime
        self.stream.writeString("AccountCreatedDate") # AccountCreatedDate
        self.stream.writeInt(0) # StartupCooldownSeconds
        self.stream.writeString("GoogleServiceId") # GoogleServiceId