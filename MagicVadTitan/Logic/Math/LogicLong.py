class LogicLong:
    def __init__(self, highInteger: int = 0, lowInteger: int = 0) -> None:
        self.highInteger = highInteger
        self.lowInteger = lowInteger

    def decode(self, stream) -> None:
        self.highInteger = stream.readInt()
        self.lowInteger = stream.readInt()

    def encode(self, encoder) -> None:
        encoder.writeInt(self.highInteger)
        encoder.writeInt(self.lowInteger)
    
    def isZero(self):
        result = False
        if self.higherInteger and self.lowerInteger == 0:
            return True
        else:
            return result
    
    def hashCode(self):
        return self.lowerInteger + 31 * self.higherInteger
    
    def equals(self, logiclong):
        if self.higherInteger == logiclong.higherInteger and self.lowerInteger == logiclong.lowerInteger:
            return True
        else:
            return False
        
    def clone(self):
        return LogicLong(self.lowerInteger, self.higherInteger)
    
    def getHigherInt(self):
        return self.higherInteger
    
    def getLowerInt(self):
        return self.lowerInteger
    
    
    def toString(self) -> str:
        return "LogicLong({0}-{1})".format(self.higherInteger, self.lowerInteger)