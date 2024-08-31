from colorama import init
init()
from colorama import Fore
class Debugger:
    @staticmethod
    def warning(msg: str):
        print(Fore.YELLOW + f"[WARNING] {msg}")

    @staticmethod
    def error(msg: str):
        print(Fore.RED + f"[ERROR] {msg}")
    
    @staticmethod
    def print(msg: str):
        print(Fore.GREEN + f"[DEBUG] {msg}")