import threading
import time
from pymongo import MongoClient
import json
from MagicVadServer.Database.Databasemanager import Account, DataBase

client = MongoClient("mongodb://localhost:27017")
db = client['MagicVad_v5']
accounts = db['accounts']

class AccountCache:
    _cached_accounts = {}
    _started = True
    _lock = threading.Lock()

    @classmethod
    def init(cls):
        cls._thread = threading.Thread(target=cls._update)
        cls._thread.start()

    @classmethod
    def _update(cls):
        while cls._started:
            cls.save_all()
            time.sleep(1)

    @classmethod
    def save_all(cls):
        with cls._lock:
            for account in cls._cached_accounts.values():
                try:
                    cls.save_account(account)
                except Exception as e:
                    print(f"Error saving account: {e}")

    @classmethod
    def save_account(cls, account):
        if account:
            account_data = json.dumps(account.__dict__, default=str)
            accounts.update_one(
                {"AccountId": account.avatarId.lowerInt},
                {"$set": {"Data": account_data}},
                upsert=True
            )

    @classmethod
    def is_account_cached(cls, account_id):
        with cls._lock:
            return account_id in cls._cached_accounts

    @classmethod
    def get_account(cls, account_id):
        with cls._lock:
            return cls._cached_accounts.get(account_id)

    @classmethod
    def cache_account(cls, account):
        with cls._lock:
            cls._cached_accounts[account.avatarId.lowerInt] = account

    @classmethod
    def stop(cls):
        cls._started = False
        cls._thread.join()
