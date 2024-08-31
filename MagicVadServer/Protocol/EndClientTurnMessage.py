from MagicVadTitan.Logic.Message.PiranhaMessage import PiranhaMessage
class EndClientTurnMessage(PiranhaMessage):
    def __init__(self) -> None:
        super().__init__(0)
        self.getCommands = 0
        self.getSubTick = 0
        self.getChecksum = 0

    def getMessageType(self) -> int:
        return 14102
    
    def decode(self):
        super().decode()
        self.getSubTick = self.stream.readInt()
        self.getChecksum = self.stream.readInt()