import asyncio
import Packets
from playground.network.packet import PacketType

Protocol = asyncio.Protocol

class ForgotPasswordServerProtocol(Protocol):
    packetCount = 0
    def __init__(self):
        self.transport = None
        self.deserializer = PacketType.Deserializer()

    def connection_made(self, transport):
        print("Echo server connected to client.")
        self.transport = transport

    def data_received(self, packet):
        print("Receiving packet")
        self.deserializer.update(packet)
        packetCount += 1
        if isinstance(packet, Packets.RequestForgotPasswordPacket()):
            print("packet")
        elif isinstance(packet, Packets.SecurityAnswerPacket()):
            print("packet")
        elif isinstance(packet, Packets.ResetPasswordInputPacket()):
            print("packet")
        else:
            print("Packet was not recognized by server. Closing socket")
            self.transport.close()
        if packetCount == 6:
            print("Closing the socket")
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

    def data_received(self, packet):
        print("Receiving packet")
        self.deserializer.update(packet)
        packetCount += 1
        if isinstance(packet, Packets.SecurityQuestionPacket()):
            print("packet")
        elif isinstance(packet, Packets.ForgotPasswordTokenPacket()):
            print("packet")
        elif isinstance(packet, Packets.PasswordResetPacket()):
            print("packet")
        else:
            print("Packet was not recognized by client. Closing socket")
            self.transport.close()
        if packetCount == 6:
            print("Closing the socket")
            self.transport.close()

    def connection_lost(self, exc):
        print("Echo client connection lost because {}".format(exc))
        self.transport = None
