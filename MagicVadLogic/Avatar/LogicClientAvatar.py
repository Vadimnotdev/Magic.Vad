from MagicVadTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from MagicVadLogic.Base.LogicBase import LogicBase
from MagicVadTitan.Logic.Math.LogicLong import LogicLong
class LogicClientAvatar():
    def __init__(self) -> None:
        self.resources = {
            3000001: 99999,  # Gold
            3000002: 99999,  # Elixir
            3000003: 99999   # Dark Elixir
        }
        self.tutorialSteps = list(range(21000000, 21000013)) # tutorial steps list
        self.idFirst = 0
        self.idSecond = 1
        self.currentHomeIdFirst = 0
        self.currentHomeIdSecond = 1
        self.allianceIdFirst = 1
        self.allianceIdSecond = 1
        
        self.allianceName = None
        self.allianceBadgeId = 0
        self.allianceRole = 0
        self.allianceExpLevel = 0
        
        self.leagueType = 16
        self.name = "vadim_not_dev"
        self.facebookId = None
        self.expLevel = 99
        self.expPoints = 999
        self.diamonds = 99999
        self.freeDiamonds = 0
        self.attackRating = 0
        self.attackFactor = 0
        self.score = 999
        #self.duelScore = 0
        self.attackWincount = 0
        self.attackLoseCount = 0
        self.defenseWinCount = 0
        self.defenseLoseCount = 0
        self.nameSetByUser = False
        self.allianceChatFilter = False
    
    def encode(self, encoder: ChecksumEncoder):
        encoder.writeInt(0) #LogicDataVersion
        encoder.writeInt(0) #HighID
        encoder.writeInt(1) #LowID
        encoder.writeInt(0) #HighAllianceId
        encoder.writeInt(1) #LowAllianceId

        
        encoder.writeBoolean(False)


        encoder.writeInt(self.leagueType)

        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(5)

        encoder.writeString(self.name)
        encoder.writeString(self.facebookId)
        
        encoder.writeInt(self.expLevel)
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

        encoder.writeInt(len(self.tutorialSteps)) # skip tutorial
        for item in self.tutorialSteps:
            encoder.writeInt(item)

        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)