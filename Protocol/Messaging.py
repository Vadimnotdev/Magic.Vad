from Messages.PiranhaMessage import PiranhaMessage
from RC4Encrypter.RC4Encrypter import RC4Encrypter
import socket

class Messaging:
    def __init__(self, client: socket.socket):
        self.client = client
        self.rc4_encrypter = RC4Encrypter()
    
   # @staticmethod
   # def printByteArray(array: bytearray):
    #    hexStr = ''.join('\\x{:02x}'.format(b) for b in array)
   #     print(f'bytearray(b\"{hexStr}\")')
    
    def sendMessage(self, message: PiranhaMessage):
        message.encode()
        encodingBytes = message.getByteStream().getByteArray()[:message.getEncodingLength()]
      #  print("Encoding Bytes:")
      #  self.printByteArray(encodingBytes)
        
        encEncodingBytes = self.rc4_encrypter.encrypt(encodingBytes)
      #  print("Encrypted Encoding Bytes:")
      #  self.printByteArray(encEncodingBytes)
        
        fullPayload = bytearray(len(encEncodingBytes) + 7)
        Messaging.writeHeader(fullPayload, message, len(encEncodingBytes))
        fullPayload[7:] = encEncodingBytes
        
        self.client.send(fullPayload)
        print("[Messaging] Sent: " + str(message.getMessageType()))
    
    def recv(self, a):
        data = bytearray()
        while len(data) < a:
            packet = self.client.recv(a - len(data))
            if not packet:
                print("Data is NULL")
                return b''
            data.extend(packet)
        return data
    
    @staticmethod
    def readHeader(buffer: bytearray):
        messageType = buffer[1] | (buffer[0] << 8)
        encodingLength = (buffer[2] << 16) | (buffer[3] << 8) | buffer[4]
        messageVersion = buffer[6] | (buffer[5] << 8)
        return messageType, encodingLength, messageVersion
    
    @staticmethod
    def writeHeader(buffer: bytearray, message: PiranhaMessage, length: int):
        messageType = message.getMessageType()
        messageVersion = message.getMessageVersion()
        buffer[0] = (messageType >> 8) & 0xFF
        buffer[1] = messageType & 0xFF
        buffer[2] = (length >> 16) & 0xFF
        buffer[3] = (length >> 8) & 0xFF
        buffer[4] = length & 0xFF
        encodingLength = message.getEncodingLength()
        if encodingLength >= 16777216:
            raise ValueError(f"Trying to send too big message, type {messageType}")
        buffer[5] = (messageVersion >> 8) & 0xFF
        buffer[6] = messageVersion & 0xFF
