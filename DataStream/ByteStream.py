from Logic.LogicLong import LogicLong
from DataStream.ChecksumEncoder import ChecksumEncoder
class ByteStream(ChecksumEncoder):
    def __init__(self, capacity: int) -> None:
        super().__init__()
        self.offset = 0
        self.length = 0
        self.bitIndex = 0
        self.buffer = bytearray(capacity)

    def destruct(self):
        self.offset = 0
        self.length = 0
        self.bitIndex = 0
        self.buffer = None

    def ensureCapacity(self, capacity: int):
        BufferLength = len(self.buffer)
        if self.offset + capacity > BufferLength:
            tmpBuffer = bytearray(BufferLength + capacity + 100)
            tmpBuffer[:BufferLength] = self.buffer
            self.buffer = tmpBuffer

    def getByteArray(self):
        return self.buffer

    def getCapacityIncrement(self):
        return 100

    def getDataPointer(self):
        return self.buffer[self.offset]

    def getLength(self):
        if self.offset < self.length:
            return self.length
        return self.offset

    def getOffset(self):
        return self.offset

    def isAtEnd(self):
        return self.offset >= self.length

    def isCheckSumOnlyMode(self):
        return False

    def readBoolean(self):
        if self.bitIndex == 0:
            self.offset = self.offset + 1
        value = (self.buffer[self.offset - 1] & (1 << self.bitIndex)) != 0
        self.bitIndex = (self.bitIndex + 1) & 7
        return value

    def readByte(self):
        self.bitIndex = 0
        self.offset = self.offset + 1
        return self.buffer[self.offset]

    def readBytes(self, length, maxCapacity):  # a2 - length a3 - maxCapacity
        self.bitIndex = 0
        if length <= -1:
            if length != -1:
                print("Negative readBytes length encountered.")
            return None
        if length <= maxCapacity:
            array: bytearray = self.buffer[self.offset: self.offset + length]
            self.offset += length
            return array

        print("readBytes too long array, max " + str(maxCapacity))
        return None

    def readBytesLength(self):
        self.bitIndex = 0
        value = (self.buffer[self.offset] << 24) | (self.buffer[self.offset + 1] <<
                                                    16) | (self.buffer[self.offset + 2] << 8) | self.buffer[self.offset + 3]
        self.offset = self.offset + 4
        return value

    def setByteArray(self, buffer: bytearray, length: int, BufferLength):
        self.offset = 0
        self.length = length
        self.bitIndex = 0
        self.buffer = buffer

    def readInt(self):
        self.bitIndex = 0
        value = (self.buffer[self.offset] << 24) | (self.buffer[self.offset + 1] <<
                                                    16) | (self.buffer[self.offset + 2] << 8) | self.buffer[self.offset + 3]
        self.offset = self.offset + 4
        return value

    def readLong(self) -> LogicLong:
        long: LogicLong = LogicLong()
        long.decode(self)
        return long

    def readShort(self):
        self.bitIndex = 0
        value = (self.buffer[self.offset] << 8) | self.buffer[self.offset + 1]
        self.offset = self.offset + 2
        return value

    def readString(self, maxCapacity: int = 900001) -> str:
        length: int = self.readBytesLength()

        if (length == -1):
            if (length != -1):
                print("Too long String encountered.")

            return None
        else:
            if (length <= maxCapacity):
                byteArray: bytearray = self.buffer[self.offset: self.offset + length]
                stringValue: str = byteArray.decode("utf-8")
                self.offset += length
                return stringValue
            
            print("Too long String encountered, max " + str(maxCapacity))

        return None
    
    def readStringReference(self, maxCapacity: int = 900000) -> str:
        length: int = self.readBytesLength()

        if (length <= -1):
            print("Negative String length encountered.")

        else:
            if (length <= maxCapacity):
                byteArray: bytearray = self.buffer[self.offset: self.offset + length]
                stringValue: str = byteArray.decode("utf-8")
                self.offset += length
                return stringValue
            
            print("Too long String encountered, max " + maxCapacity)
        
        return ""

    def removeByteArray(self):
        self.buffer = None
        return self.buffer

    def resetOffset(self):
        self.offset = 0
        self.bitIndex = 0

    def setOffset(self, offset):
        self.offset = offset
        self.bitIndex = 0

    def writeBoolean(self, value: bool):
        super().writeBoolean(value)
        if self.bitIndex == 0:
            self.ensureCapacity(1)
            self.buffer[self.offset] = 0
            self.offset += 1

        if value:
            self.buffer[self.offset - 1] |= (1 << self.bitIndex) & 0xFF
            self.bitIndex = (self.bitIndex + 1) & 7

    def writeByte(self, value: int):
        super().writeByte(value)
        self.bitIndex = 0
        self.buffer[self.offset] = value
        self.offset = self.offset + 1
    
    def writeBytes(self, value: bytearray, length: int):
        super().writeBytes(value, length)
        if value is None:
            self.writeInt(-1)
        else:
            self.ensureCapacity(length + 4)
            self.writeInt(length)
            self.buffer[self.offset:self.offset + length] = value
            self.offset += length
    
    def writeIntToByteArray(self, value):
        self.ensureCapacity(4)
        self.bitIndex = 0
        self.buffer[self.offset] = (value >> 24) & 0xFF
        self.buffer[self.offset + 1] = (value >> 16) & 0xFF
        self.buffer[self.offset + 2] = (value >> 8) & 0xFF
        self.buffer[self.offset + 3] = value & 0xFF
        self.offset += 4
    
    def writeInt(self, value):
        super().writeInt(value)
        self.writeIntToByteArray(value)
    
    def writeShort(self, value):
        super().writeShort(self, value)
        self.ensureCapacity(2)
        self.offset = self.offset + 1
        self.buffer[self.offset] = (value >> 8) & 0xFF
        self.buffer[self.offset + 1] = value & 0xFF
        self.offset = self.offset + 2
    
    def writeString(self, value: str):
        super().writeString(value)

        if (value is None):
            self.writeInt(-1)

        else:
            bytesValue: bytes = value.encode("utf-8")
            length: int = len(bytesValue)

            if (length <= 900001):
                self.ensureCapacity(length + 4)
                self.writeInt(length)

                self.buffer[self.offset:self.offset + length] = bytesValue
                self.offset += length
            else:
                print("ByteStream::writeString invalid string length " + str(length))
                self.writeInt(-1)
    
    def writeStringReference(self, value):
        super().writeStringReference(self, value)
        bytesValue: bytes = value.encode('utf-8')
        length = len(bytesValue)
        if length >= 900001:
            self.ensureCapacity(length + 4)
            self.writeIntToByteArray(length)
            self.buffer[self.offset:self.offset + length] = bytesValue
            self.offset = self.offset + length
        else:
            print("ByteStream::writeString invalid string length", length)
            return self.writeIntToByteArray(-1)
    
    def clear(self, capacity):
        if self.buffer is not None:
            self.buffer = None
        self.offset = 0
        self.length = 0
        self.bitIndex = 0
        self.buffer = None
        
        if capacity > 4294967295:
            capacity = 4294967295
        self.buffer = bytearray(capacity)  
        self.bufferLength = capacity
        return self.buffer