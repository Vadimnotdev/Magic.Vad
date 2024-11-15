from MagicVadServer.Protocol.LogicCommand import LogicCommand
from MagicVadTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from MagicVadServer.Protocol.LogicCommandManager import LogicCommandManager

class AvailableServerCommandMessage(PiranhaMessage):
    
    def __init__(self, message_version=0):
        super().__init__(message_version)
        self.server_command = None

    def encode(self):
        super().encode()
        command_manager = LogicCommandManager(self.server_command)
        command_manager.encode_command(self.stream)

    def get_message_type(self):
        return 24111

    def get_service_node_type(self):
        return 10
    
    def remove_server_command(self):
        temp = self.server_command
        self.server_command = None
        return temp

    def set_server_command(self, command):
        self.server_command = command
