import asyncio
import Packets
from playground.network.packet import PacketType

Protocol = asyncio.Protocol

class ForgotPasswordServerProtocol(Protocol):
    def __init__(self):
        self.transport = None
        self.deserializer = PacketType.Deserializer()

    def connection_made(self, transport):
        print("Echo server connected to client.")
        self.transport = transport

    def data_received(self, data):
        print("Receiving packet")
        self.deserializer.update(data)
        packet = PacketType.Deserialize(data)
        if isinstance(packet, Packets.RequestForgotPasswordPacket):
            print("packet1")
        elif isinstance(packet, Packets.SecurityAnswerPacket):
            print("packet3")
        elif isinstance(packet, Packets.ResetPasswordInputPacket):
            print("packet5")
        else:
            print("Packet was not recognized by server. Closing socket")
            self.transport.close()

    def connection_lost(self, exc):
        print("Echo server connection lost because {}".format(exc))
        self.transport = None

class ForgotPasswordClientProtocol(Protocol):
    def __init__(self):
        self.transport = None
        self.deserializer = PacketType.Deserializer()

    def connection_made(self, transport):
        print("Echo server connected to client.")
        self.transport = transport

    def data_received(self, data):
        print("Receiving packet")
        self.deserializer.update(data)
        packet = PacketType.Deserialize(data)
        if isinstance(packet, Packets.SecurityQuestionPacket):
            print("packet2")
        elif isinstance(packet, Packets.ForgotPasswordTokenPacket):
            print("packet4")
        elif isinstance(packet, Packets.PasswordResetPacket):
            print("packet6")
        else:
            print("Packet was not recognized by client. Closing socket")
            self.transport.close()


    def connection_lost(self, exc):
        print("Echo client connection lost because {}".format(exc))
        self.transport = None
