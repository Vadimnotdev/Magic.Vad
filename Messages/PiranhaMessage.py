from DataStream.ByteStream import ByteStream
class PiranhaMessage:
    def __init__(self, messageVersion) -> None:
        self.stream = ByteStream(10)
        self.messageVersion = messageVersion

    def encode(self):
        pass

    def decode(self):
        pass

    def isClientToServerMessage(self):
        return self.getMessageType() - 10000 < 10000
    
    def isServerToClientMessage(self):
        return self.getMessageType() - 20000 < 10000
    
    def getMessageBytes(self):
        return self.stream.getByteArray()
    
    def getByteStream(self):
        return self.stream
    
    def getEncodingLength(self):
        return self.stream.getLength()

    def getMessageType(self) -> int:
        return 0
    
    def getMessageVersion(self):
        return self.messageVersion
    
    def setMessageVersion(self, messageVersion):
        self.messageVersion = messageVersion

    def destruct(self):
        self.stream.destruct()
    
    def clear(self, capacity):
        return self.stream.clear(capacity)