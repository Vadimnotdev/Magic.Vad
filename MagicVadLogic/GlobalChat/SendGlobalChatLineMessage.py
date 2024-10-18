from MagicVadTitan.Logic.Message.PiranhaMessage import PiranhaMessage


class SendGlobalChatLineMessage(PiranhaMessage):
    def __init__(self):
        super().__init__(0)
        self.message = ""

    def getMessageType(self) -> int:
        return 14715

    def decode(self):
        super().decode()
        self.message = self.stream.readString()

    def getMessage(self):
        return self.message

    def setMessage(self, message: str):
        self.message = message

    def getServiceNodeType(self):
        return 6