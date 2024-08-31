import socket
import threading
import traceback
from MagicVadServer.Protocol.Messaging import Messaging
from MagicVadTitan.Encryption.RC4Encrypter import RC4Encrypter
from MagicVadTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from MagicVadLogic.LogicMagicMessageFactory import LogicMagicMessageFactory
from MagicVadServer.Protocol.MessageManager import MessageManager

class Connection(threading.Thread):
    def __init__(self, socket: socket.socket, address):
        super().__init__()
        self.client = socket
        self.address = address
        self.messaging = Messaging(self.client)
        self.manager = MessageManager(self.messaging)
        self.rc4_encrypter = RC4Encrypter()
    
    def recv(self, n) -> bytearray:
        data = bytearray()
        while len(data) < n:
            packet = self.client.recv(n - len(data))
            if not packet:
                print("Data is NULL")
                return b''
            data.extend(packet)
        return data
    
    def run(self) -> None:
        try:
            while True:
                header = self.client.recv(7)
                
                if len(header) >= 7:
                    messageType, encodingLength, messageVersion = self.messaging.readHeader(header)
                    payload = self.recv(encodingLength)
                    decPayload = self.rc4_encrypter.decrypt(payload)
                    
                    message: PiranhaMessage = LogicMagicMessageFactory.createMessageByType(messageType)

                    if message is not None:
                        message.setMessageVersion(messageVersion)
                        message.getByteStream().setByteArray(decPayload, encodingLength, len(decPayload))

                        message.decode()

                        self.manager.receiveMessage(message)
                    else:
                        print(f"[Connection] Ignoring message of unknown type {messageType}")

        except ConnectionError:
            print(f"Client {self.address[0]}:{self.address[1]} has disconnected")
            self.client.close()
        except Exception as e:
            print("Error: " + str(e))
            traceback.print_exc()
