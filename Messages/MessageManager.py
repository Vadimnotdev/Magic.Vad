from Messages.Login.LoginMessage import LoginMessage
from Messages.PiranhaMessage import PiranhaMessage
from Protocol.Messaging import Messaging
from Messages.Login.LoginOkMessage import LoginOkMssage
from Messages.OwnHomeDataMessage import OwnHomeDataMessage

class MessageManager:
    def __init__(self, messaging: Messaging) -> None:
        self.messaging = messaging
    
    def receiveMessage(self, message: PiranhaMessage):
        messageType = message.getMessageType()

        if messageType == 10101:
            self.onLoginMessage(self, message)
        elif messageType == 14102:
            pass
        else:
            print("Unknown message type: " + str(messageType))

        
    def toString(self) -> str:
        return "{0}-{1}".format(self.highInteger, self.lowInteger)

    def onLoginMessage(self, message, loginMessage: LoginMessage):
        print(f"[MessageManager] Logged in! AccountId: {loginMessage.accountId.toString()} PassToken: {loginMessage.passToken} ClientMajorVersion: {loginMessage.ClientMajorVersion} ClientBuild: {loginMessage.ClientBuild} ResourceSha: {loginMessage.ResourceSha}")

        self.messaging.sendMessage(LoginOkMssage())
        self.messaging.sendMessage(OwnHomeDataMessage())


        if isinstance(message, LoginMessage):
            
            print("Login message received")
        else:
            print("Received message of wrong type for onLoginMessage")

