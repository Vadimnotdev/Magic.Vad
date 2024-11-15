from MagicVadLogic.Message.Account.LoginMessage import LoginMessage
from MagicVadTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from MagicVadServer.Protocol.Messaging import Messaging
from MagicVadLogic.Message.Account.LoginOkMessage import LoginOkMessage
from MagicVadLogic.Message.Home.OwnHomeDataMessage import OwnHomeDataMessage
from MagicVadLogic.Profile.AvatarProfileMessage import AvatarProfileMessage
from MagicVadLogic.GlobalChat.GlobalChatLineMessage import GlobalChatLineMessage
from MagicVadLogic.GlobalChat.SendGlobalChatLineMessage import SendGlobalChatLineMessage
from MagicVadLogic.Message.Home.ChangeAvatarNameMessage import ChangeAvatarNameMessage
from MagicVadServer.Database.Databasemanager import *



class MessageManager:
    def __init__(self, messaging: Messaging) -> None:
        self.messaging = messaging

    def receiveMessage(self, message: PiranhaMessage, database: DataBase):
        messageType = message.getMessageType()

        if messageType == 10101:
            self.onLoginMessage(self, message, database)

        elif messageType == 14325:
            self.messaging.sendMessage(AvatarProfileMessage(database))
        elif messageType == 14715:
            self.onSendGlobalChatMessage(message, database)
        elif messageType == 14102:
            pass
        elif messageType == 10212:
            self.ChngeAvatarNameRecived(message, database)

        else:
            print("Unknown message type: " + str(messageType))

    def __str__(self) -> str:
        return f"{self.highInteger}-{self.lowInteger}"

    def onLoginMessage(self, message, loginMessage: LoginMessage, database: DataBase):
        if loginMessage.avatarLowId != 0:
            print(f"Account found with avatarLowId: {
                  loginMessage.avatarLowId}. Loading account...")
            database.load_account()
        else:
            print("No existing account, creating a new account...")
            database.create_account()
        print(f"[MessageManager] Logged in! AccountId: {loginMessage.avatarLowId.__str__()} PassToken: {loginMessage.passToken} ClientMajorVersion: {
              loginMessage.ClientMajorVersion} ClientBuild: {loginMessage.ClientBuild} ResourceSha: {loginMessage.ResourceSha}")
        self.messaging.sendMessage(LoginOkMessage(database))
        self.messaging.sendMessage(OwnHomeDataMessage(database))

        if isinstance(message, LoginMessage):
            print("Login message received")
        else:
            print("Received message of wrong type for onLoginMessage")

    def onSendGlobalChatMessage(self, sendGlobalChatLineMessage: SendGlobalChatLineMessage, database: DataBase):
        print(f"New message: {sendGlobalChatLineMessage.getMessage()}")

        globalChatLineMessage = GlobalChatLineMessage(database)
        globalChatLineMessage.setMessage(
            sendGlobalChatLineMessage.getMessage())
        self.messaging.sendMessage(globalChatLineMessage)

    def ChngeAvatarNameRecived(self, message: ChangeAvatarNameMessage, database: DataBase):
        own_home_data_message = OwnHomeDataMessage(database)
        own_home_data_message.clientAvatar.avatarName = message.avatarName
        database.change_avatar_name(own_home_data_message.clientAvatar.avatarName)
        own_home_data_message.clientAvatar.tutorialSteps = list(range(21000000, 21000013))
        self.messaging.sendMessage(own_home_data_message)

