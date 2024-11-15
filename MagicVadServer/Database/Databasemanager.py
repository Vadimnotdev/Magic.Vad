from MagicVadTitan.Logic.Math.LogicLong import LogicLong
from pymongo import MongoClient
import random
import string
import json

client = MongoClient("mongodb://localhost:27017")
db = client['MagicVad_v5']
accounts = db['accounts']

class Account:
    AvatarIdCounter = 0

    @staticmethod
    def get_max_avatar_id():
        max_account = accounts.find_one(sort=[("avatarLowId", -1)])
        if max_account and 'avatarLowId' in max_account:
            return max_account['avatarLowId']
        return 0

    @classmethod
    def initialize_avatar_id_counter(cls):
        cls.AvatarIdCounter = cls.get_max_avatar_id()


class DataBase:
    def __init__(self) -> None:
        self.gold = 9999999
        self.elixir = 9999999
        self.darkElixir = 9999999
        self.resources = {
            3000001: self.gold,  # Gold
            3000002: self.elixir,  # Elixir
            3000003: self.darkElixir   # Dark Elixir
        }
        self.avatarHighId = 0
        self.avatarLowId = 0
        self.homeHighId = 0
        self.homeLowId = 0
        self.passToken = ""

        # Alliance-related attributes
        self.isInAlliance = False
        self.allianceId = None
        self.allianceName = None
        self.allianceBadgeId = None
        self.allianceRole = 0
        self.allianceExpLevel = 0

        # Avatar-related attributes
        self.avatarLeagueType = 0
        self.avatarName = ""
        self.facebookId = None
        self.avatarExpLevel = 1
        self.expPoints = 10
        self.diamonds = 99999
        self.freeDiamonds = 0
        self.attackRating = 0
        self.attackFactor = 0
        self.score = 999
        self.attackWincount = 0
        self.attackLoseCount = 0
        self.defenseWinCount = 0
        self.defenseLoseCount = 0
        self.nameSetByUser = True
        self.allianceChatFilter = False
        self.homeJSON = ""
        self.shieldDurationSeconds = 0
        self.defenseRating = 0
        self.defenseKFactor = 0

    def change_avatar_name(self, new_avatar_name: str):
        result = accounts.update_one(
            {'avatarLowId': self.avatarLowId},
            {'$set': {'avatarName': new_avatar_name}} 
        )
        
        if result.modified_count > 0:
            self.avatarName = new_avatar_name  
            self.load_account()
            print(f"Avatar name changed to {new_avatar_name}")
        else:
            print("No changes made to the avatar name.")


    def load_account(self):
        user_data = accounts.find_one({'avatarLowId': self.avatarLowId})
        if user_data:
            self.passToken = user_data["passToken"]
            self.gold = user_data["gold"]
            self.elixir = user_data["elixir"]
            self.darkElixir = user_data["darkElixir"]
            self.avatarHighId = user_data["avatarHighId"]
            self.avatarLowId = user_data["avatarLowId"]
            self.homeHighId = user_data["homeHighId"]
            self.homeLowId = user_data["homeLowId"]
            self.isInAlliance = user_data["isInAlliance"]
            self.allianceId = user_data["allianceId"]
            self.allianceName = user_data["allianceName"]
            self.allianceBadgeId = user_data["allianceBadgeId"]
            self.allianceRole = user_data["allianceRole"]
            self.allianceExpLevel = user_data["allianceExpLevel"]
            self.avatarLeagueType = user_data["avatarLeagueType"]
            self.avatarName = user_data["avatarName"]
            self.facebookId = user_data["facebookId"]
            self.avatarExpLevel = user_data["avatarExpLevel"]
            self.expPoints = user_data["expPoints"]
            self.diamonds = user_data["diamonds"]
            self.freeDiamonds = user_data["freeDiamonds"]
            self.attackRating = user_data["attackRating"]
            self.attackFactor = user_data["attackFactor"]
            self.score = user_data["score"]
            self.attackWincount = user_data["attackWincount"]
            self.defenseWinCount = user_data["defenseWinCount"]
            self.attackLoseCount = user_data["attackLoseCount"]
            self.defenseLoseCount = user_data["defenseLoseCount"]
            self.nameSetByUser = user_data["nameSetByUser"]
            self.allianceChatFilter = user_data["allianceChatFilter"]
            self.homeJSON = user_data["homeJSON"]
            self.shieldDurationSeconds = user_data["shieldDurationSeconds"]
            self.defenseRating = user_data["defenseRating"]
            self.defenseKFactor = user_data["defenseKFactor"]
        print("account is loaded")

    def create_account(self):
        Account.AvatarIdCounter += 1
        self.avatarLowId = Account.AvatarIdCounter
        self.passToken = self.passToken = ''.join(random.choices(string.ascii_lowercase + string.digits, k=40))
        home_json_data = """{"buildings":[{"data":1000001,"lvl":10,"x":21,"y":20},{"data":1000004,"lvl":0,"x":20,"y":16,"res_time":8992},{"data":1000000,"lvl":0,"x":26,"y":19,"units":[],"storage_type":0},{"data":1000015,"lvl":0,"x":18,"y":20},{"data":1000014,"lvl":0,"locked":true,"x":25,"y":32}],"obstacles":[{"data":8000007,"x":5,"y":13},{"data":8000007,"x":15,"y":29},{"data":8000008,"x":7,"y":7},{"data":8000005,"x":29,"y":4},{"data":8000006,"x":15,"y":37},{"data":8000000,"x":20,"y":4},{"data":8000008,"x":15,"y":22},{"data":8000005,"x":37,"y":18},{"data":8000007,"x":6,"y":4},{"data":8000003,"x":26,"y":10},{"data":8000004,"x":21,"y":9},{"data":8000008,"x":32,"y":21},{"data":8000005,"x":20,"y":36},{"data":8000003,"x":29,"y":34},{"data":8000005,"x":5,"y":29},{"data":8000005,"x":8,"y":10},{"data":8000005,"x":5,"y":17},{"data":8000002,"x":4,"y":33},{"data":8000002,"x":5,"y":21},{"data":8000002,"x":10,"y":32},{"data":8000008,"x":5,"y":37},{"data":8000001,"x":9,"y":4},{"data":8000001,"x":13,"y":31},{"data":8000001,"x":7,"y":35},{"data":8000007,"x":4,"y":9},{"data":8000004,"x":9,"y":23},{"data":8000004,"x":6,"y":26},{"data":8000003,"x":35,"y":21},{"data":8000005,"x":32,"y":28},{"data":8000005,"x":34,"y":13},{"data":8000001,"x":14,"y":18},{"data":8000001,"x":35,"y":5},{"data":8000012,"x":24,"y":30},{"data":8000012,"x":31,"y":10},{"data":8000010,"x":26,"y":38},{"data":8000010,"x":14,"y":5},{"data":8000013,"x":34,"y":33},{"data":8000013,"x":13,"y":9},{"data":8000014,"x":10,"y":17},{"data":8000014,"x":24,"y":7},{"data":8000006,"x":36,"y":26},{"data":8000011,"x":23,"y":34},{"data":8000011,"x":24,"y":37},{"data":8000000,"x":27,"y":35},{"data":8000000,"x":25,"y":35},{"data":8000000,"x":26,"y":30},{"data":8000007,"x":23,"y":32},{"data":8000001,"x":28,"y":31},{"data":8000014,"x":28,"y":29}],"traps":[],"decos":[],"respawnVars":{"secondsFromLastRespawn":0,"respawnSeed":1529463799,"obstacleClearCounter":0},"cooldowns":[]}"""
        self.homeJSON = home_json_data
        data = {
            "passToken": self.passToken,
            "avatarHighId": 0,
            "avatarLowId": self.avatarLowId,
            "homeHighId": 0,
            "homeLowId": self.avatarLowId,
            "gold": 9999999,
            "elixir": 9999999,
            "darkElixir": 9999999,
            "diamonds": 9999999,
            "freeDiamonds": 0,
            "score": 999,
            "avatarLeagueType": 16,
            "avatarName": "",
            "facebookId": "facebookId",
            "avatarExpLevel": 1,
            "expPoints": 10,
            "isInAlliance": False,
            "allianceId": None,
            "allianceName": None,
            "allianceBadgeId": None,
            "allianceRole": None,
            "allianceExpLevel": None,
            "attackRating": 0,
            "attackFactor": 0,
            "attackWincount": 0,
            "attackLoseCount": 0,
            "defenseWinCount": 0,
            "defenseLoseCount": 0,
            "nameSetByUser": True,
            "allianceChatFilter": False,
            "homeJSON": home_json_data,
            "shieldDurationSeconds": 0,
            "defenseRating": 0,
            "defenseKFactor": 0
        }
        accounts.insert_one(data)
        self.load_account()
        print("account is created")
        return self.passToken