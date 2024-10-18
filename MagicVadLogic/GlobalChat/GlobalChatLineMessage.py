from MagicVadTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from MagicVadTitan.Logic.Math.LogicLong import LogicLong

class GlobalChatLineMessage(PiranhaMessage):
    def __init__(self) -> None:
        super().__init__(0)
        self.message = ""
        self.avatarName = "vadim_not_dev"
        self.avatarExpLevel = 99
        self.avatarLeagueType = 16
        self.avatarId = LogicLong(0, 1)
        self.homeId = LogicLong(0, 1)
        self.allianceId = None
        self.isInAlliance = False
        self.allianceName = None
        self.allianceBadgeId = None

    def getMessageType(self) -> int:
        return 24715

    def setMessage(self, message: str) -> None:
        self.message = message

    def encode(self):
        super().encode()
        self.stream.writeString(self.message)
        self.stream.writeString(self.avatarName)
        self.stream.writeInt(self.avatarExpLevel)
        self.stream.writeInt(self.avatarLeagueType)
        self.stream.writeLong(self.avatarId)
        self.stream.writeLong(self.homeId)
        if self.isInAlliance == True:
            self.stream.writeBoolean(True)
            self.stream.writeLong(self.allianceId)
            self.stream.writeString(self.allianceName)
            self.stream.writeInt(self.allianceBadgeId)
        else:
            self.stream.writeBoolean(False)

    def getServiceNodeType(self):
        return 6
    