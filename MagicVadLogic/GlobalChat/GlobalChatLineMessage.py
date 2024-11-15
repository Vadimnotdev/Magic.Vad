from MagicVadTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from MagicVadTitan.Logic.Math.LogicLong import LogicLong
from MagicVadServer.Database.Databasemanager import *
class GlobalChatLineMessage(PiranhaMessage):
    def __init__(self, database: DataBase) -> None:
        super().__init__(0)
        self.message = ""
        self.database = database


    def load_account_data(self):
        self.database.load_account()
        self.avatarHighId = self.database.avatarHighId
        self.avatarLowId = self.database.avatarLowId
        self.homeHighId = self.database.homeHighId
        self.homeLowId = self.database.homeLowId
        self.avatarLeagueType = self.database.avatarLeagueType
        self.avatarName = self.database.avatarName
        self.avatarExpLevel = self.database.avatarExpLevel
        self.score = self.database.score
        self.allianceId = None
        self.allianceName = None
        self.allianceBadgeId = None
        self.isInAlliance = None

    def getMessageType(self) -> int:
        return 24715

    def setMessage(self, message: str) -> None:
        self.message = message

    def encode(self):
        super().encode()
        self.load_account_data()
        self.stream.writeString(self.message)
        self.stream.writeString(self.avatarName)
        self.stream.writeInt(self.avatarExpLevel)
        self.stream.writeInt(self.avatarLeagueType)
        self.stream.writeInt(self.avatarLowId)
        self.stream.writeInt(self.avatarHighId)
        self.stream.writeInt(self.avatarLowId)
        self.stream.writeInt(self.homeHighId)
        if self.isInAlliance == True:
            self.stream.writeBoolean(True)
            self.stream.writeLong(self.allianceId)
            self.stream.writeString(self.allianceName)
            self.stream.writeInt(self.allianceBadgeId)
        else:
            self.stream.writeBoolean(False)

    def getServiceNodeType(self):
        return 6
    