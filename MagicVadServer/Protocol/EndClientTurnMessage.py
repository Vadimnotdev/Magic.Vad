from MagicVadTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from MagicVadTitan.Logic.Debug.Debugger import Debugger


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
        self.SubTick = self.stream.readInt()
        self.Checksum = self.stream.readInt()
        array_size = self.stream.readInt()

        if array_size <= 1024:
            if array_size > 0:
                self.commands = []

                while array_size > 0:
                    command = None  # LogicCommandManager.decode(self.stream)

                    if command is None:
                        break

                    self.commands.append(command)
                    array_size -= 1
        else:
            Debugger.error(
                f"EndClientTurn::decode() command count is too high! ({array_size})")
