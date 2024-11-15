from MagicVadTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from MagicVadServer.Database.Databasemanager import *

class LoginOkMessage(PiranhaMessage):
    def __init__(self, database: DataBase):
        super().__init__(0)
        self.database = database
        self.avatarHighId = 0
        self.avatarLowId = 0
        self.homeHighId = 0
        self.homeLowId = 0
        self.passToken = ""
        Account.initialize_avatar_id_counter()

    def getMessageType(self) -> int:
        return 20104
    
    def load_account_data(self):
        self.database.load_account()
        self.avatarHighId = self.database.avatarHighId
        self.avatarLowId = self.database.avatarLowId
        self.homeHighId = self.database.homeHighId
        self.homeLowId = self.database.homeLowId
        self.passToken = self.database.passToken

    def encode(self):
        super().encode()
        self.load_account_data()
        self.stream.writeInt(self.avatarHighId)  # AvatarHighID
        self.stream.writeInt(self.avatarLowId)  # AvatarLowId
        self.stream.writeInt(self.homeHighId)  # HomeHighID
        self.stream.writeInt(self.homeLowId)  # HomeLowId
        self.stream.writeString(self.passToken)
        self.stream.writeString("FacebookAppId")
        self.stream.writeString("GamecenterId")
        self.stream.writeInt(5)  # ServerMajorVersion
        self.stream.writeInt(2)  # ServerBuild
        self.stream.writeInt(4)  # ContentVersion
        self.stream.writeString("dev")  # ServerEnvironment
        self.stream.writeInt(1)  # SessionCount
        self.stream.writeInt(1)  # PlayTimeSeconds
        self.stream.writeInt(0)  # DaysSinceStartedPlaying
        self.stream.writeString("FacebookAppId")
        self.stream.writeString("ServerTime")
        self.stream.writeString("AccountCreatedDate")
        self.stream.writeInt(0)  # StartupCooldownSeconds
        self.stream.writeString("GoogleServiceId")
