from MagicVadLogic.Message.Account.LoginMessage import LoginMessage
from MagicVadServer.Protocol.EndClientTurnMessage import EndClientTurnMessage
from MagicVadLogic.Profile.AskForAvatarProfileMessage import AskForAvatarProfileMessage
class LogicMagicMessageFactory:
    messages = {
        10101: LoginMessage,
        14102: EndClientTurnMessage,
        14325: AskForAvatarProfileMessage
        }
    def createMessageByType(messageType):
        messages = LogicMagicMessageFactory.messages
        if (messageType in LogicMagicMessageFactory.messages.keys()):
            if (type(messages[messageType]) is None):
                pass
            else:
                print("[LogicMagicMessageFactory]", str(messageType) + " created")
                return messages[messageType]()
        else:
            return None