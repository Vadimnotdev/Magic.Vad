from MagicVadTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from MagicVadTitan.Logic.Math.LogicLong import LogicLong
from MagicVadLogic.Base.LogicBase import LogicBase
from MagicVadServer.Database.Databasemanager import *
class LogicClientHome(LogicBase):
    def __init__(self, database: DataBase):
        super().__init__()
        self.database = database
        self.homeHighId = 0
        self.homeLowId = 0
        self.homeJSON = ""
        self.shieldDurationSeconds = 0
        self.defenseRating = 0
        self.defenseKFactor = 0
        Account.initialize_avatar_id_counter()

    def load_account_data(self):
        self.database.load_account()
        self.homeHighId = self.database.homeHighId
        self.homeLowId = self.database.homeLowId
        self.homeJSON = self.database.homeJSON
        self.shieldDurationSeconds = self.database.shieldDurationSeconds
        self.defenseRating = self.database.defenseRating
        self.defenseKFactor = self.database.defenseKFactor

    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        self.load_account_data()
        encoder.writeInt(self.homeHighId)
        encoder.writeInt(self.homeLowId)
        encoder.writeString(self.homeJSON)
        encoder.writeInt(self.shieldDurationSeconds) # ShieldDurationSeconds
        encoder.writeInt(self.defenseRating) # DefenseRating
        encoder.writeInt(self.defenseKFactor) # DefenseKFactor