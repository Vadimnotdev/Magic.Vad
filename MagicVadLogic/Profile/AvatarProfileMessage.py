from MagicVadTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from MagicVadLogic.Avatar.LogicClientAvatar import LogicClientAvatar


class AvatarProfileMessage(PiranhaMessage):
    def __init__(self):
        super().__init__(0)
        self.snapshotChecksum = 0

    def getMessageType(self) -> int:
        return 24334

    def getServiceNodeType(self) -> int:
        return 9

    def encode(self):
        LogicClientAvatar().encode(self.stream)
