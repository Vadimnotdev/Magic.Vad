from MagicVadTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from MagicVadLogic.Base.LogicBase import LogicBase
from MagicVadTitan.Logic.Math.LogicLong import LogicLong
from MagicVadServer.Database.Databasemanager import *
from MagicVadLogic.Message.Account.LoginMessage import LoginMessage

class LogicClientAvatar:
    def __init__(self, database: DataBase):
        self.database = database
        self.resources = {
            3000001: 0,  # Gold
            3000002: 0,  # Elixir
            3000003: 0   # Dark Elixir
        }
        self.avatarHighId = 0
        self.avatarLowId = 0
        self.homeHighId = 0
        self.homeLowId = 0
        self.currentHomeIdFirst = 0
        self.currentHomeIdSecond = 1

        self.isInAlliance = False
        self.allianceId = None
        self.allianceName = None
        self.allianceBadgeId = None
        self.allianceRole = 0
        self.allianceExpLevel = 0

        self.avatarLeagueType = 0
        self.avatarName = ""
        self.facebookId = None
        self.avatarExpLevel = 1
        self.expPoints = 0
        self.diamonds = 0
        self.freeDiamonds = 0
        self.attackRating = 0
        self.attackFactor = 0
        self.score = 999
        self.attackWincount = 0
        self.attackLoseCount = 0
        self.defenseWinCount = 0
        self.defenseLoseCount = 0
        self.nameSetByUser = False
        self.allianceChatFilter = False
        self.database.load_account()
        if database.avatarName == "":
            x = 21000010
        else:
            x = 21000013
        self.tutorialSteps = list(range(21000000, x))  # tutorial steps list
        Account.initialize_avatar_id_counter()


        
    def load_account_data(self):
        self.database.load_account()
        self.avatarHighId = self.database.avatarHighId
        self.avatarLowId = self.database.avatarLowId
        self.homeHighId = self.database.homeHighId
        self.homeLowId = self.database.homeLowId
        self.avatarLeagueType = self.database.avatarLeagueType
        self.avatarName = self.database.avatarName
        self.facebookId = self.database.facebookId
        self.avatarExpLevel = self.database.avatarExpLevel
        self.expPoints = self.database.expPoints
        self.diamonds = self.database.diamonds
        self.freeDiamonds = self.database.freeDiamonds
        self.attackRating = self.database.attackRating
        self.attackFactor = self.database.attackFactor
        self.score = self.database.score
        self.attackWincount = self.database.attackWincount
        self.attackLoseCount = self.database.attackLoseCount
        self.defenseWinCount = self.database.defenseWinCount
        self.defenseLoseCount = self.database.defenseLoseCount
        self.resources = {
            3000001: self.database.gold,  # Gold
            3000002: self.database.elixir,  # Elixir
            3000003: self.database.darkElixir   # Dark Elixir
        }

    def encode(self, encoder: ChecksumEncoder):
        self.load_account_data()
        encoder.writeInt(0)  # LogicDataVersion
        encoder.writeInt(self.avatarHighId)  # AvatarHighID
        encoder.writeInt(self.avatarLowId)  # AvatarLowId
        encoder.writeInt(self.avatarHighId)  # HomeHighID
        encoder.writeInt(self.avatarLowId)  # HomeLowId
        encoder.writeBoolean(False)
        encoder.writeInt(self.avatarLeagueType)

        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)

        encoder.writeString(self.avatarName)
        encoder.writeString(self.facebookId)

        encoder.writeInt(self.avatarExpLevel)
        encoder.writeInt(self.expPoints)
        encoder.writeInt(self.diamonds)
        encoder.writeInt(self.freeDiamonds)
        encoder.writeInt(self.attackRating)
        encoder.writeInt(self.attackFactor)
        encoder.writeInt(self.score)
        encoder.writeInt(self.attackWincount)
        encoder.writeInt(self.attackLoseCount)
        encoder.writeInt(self.defenseWinCount)
        encoder.writeInt(self.defenseLoseCount)
        encoder.writeBoolean(False)
        encoder.writeInt(0)

        encoder.writeInt(0)

        encoder.writeInt(len(self.resources))
        for resource_id, amount in self.resources.items():
            encoder.writeInt(resource_id)
            encoder.writeInt(amount)

        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)

        encoder.writeInt(len(self.tutorialSteps))  # skip tutorial
        for item in self.tutorialSteps:
            encoder.writeInt(item)

        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
