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
    
    def isZero(self):
        result = False
        if self.higherInt and self.lowerInt == 0:
            return True
        else:
            return result
    
    def hashCode(self):
        return self.lowerInt + 31 * self.higherInt
    
    def equals(self, logiclong):
        if self.higherInt == logiclong.higherInt and self.lowerInt == logiclong.lowerInt:
            return True
        else:
            return False
        
    def clone(self):
        return LogicLong(self.lowerInt, self.higherInt)
    
    def getHigherInt(self):
        return self.higherInt
    
    def getLowerInt(self):
        return self.lowerInt
    
    def __str__(self) -> str:
        return f"{self.higherInt}-{self.lowerInt}"