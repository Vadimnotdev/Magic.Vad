from MagicVadTitan.Logic.Message.PiranhaMessage import PiranhaMessage


class AskForAvatarProfileMessage(PiranhaMessage):
    def __init__(self):
        super().__init__(0)
        self.snapshotChecksum = 0
        self.avatarId = 0
        self.homeId = 0

    def getMessageType(self) -> int:
        return 14325

    def decode(self):
        self.stream.readLong() #avatarId
        self.stream.readLong() #homeId

