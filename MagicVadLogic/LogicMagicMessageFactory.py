from MagicVadLogic.Message.Account.LoginMessage import LoginMessage
from MagicVadServer.Protocol.EndClientTurnMessage import EndClientTurnMessage
from MagicVadLogic.Profile.AskForAvatarProfileMessage import AskForAvatarProfileMessage
from MagicVadLogic.GlobalChat.SendGlobalChatLineMessage import SendGlobalChatLineMessage
from MagicVadLogic.Message.Home.ChangeAvatarNameMessage import ChangeAvatarNameMessage

class LogicMagicMessageFactory:
    messages = {
        10101: LoginMessage,
        14102: EndClientTurnMessage,
        14325: AskForAvatarProfileMessage,
        14715: SendGlobalChatLineMessage,
        10212: ChangeAvatarNameMessage
        }
    def createMessageByType(messageType):
        messages = LogicMagicMessageFactory.messages
        if (messageType in LogicMagicMessageFactory.messages.keys()):
            if (type(messages[messageType]) is None):
                pass
            else:
                return messages[messageType]()
        else:
            return None