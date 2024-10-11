class LogicLong:
    def __init__(self, lowerInt=0, higherInt=0):
        self.higherInt = higherInt
        self.lowerInt = lowerInt

    def decode(self, stream): #Wisedev told me choose Stream name for arg
        self.higherInt = stream.readInt()
        self.lowerInt = stream.readInt()

    def encode(self, encoder):
        encoder.writeInt(self.higherInt)
        encoder.writeInt(self.lowerInt)
    
    
    def __str__(self) -> str:
        return f"{self.higherInt}-{self.lowerInt}"