from MagicVadTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
class LogicBase:
    def encode(self, encoder: ChecksumEncoder):
        encoder.writeInt(0) #LogicDataVersion