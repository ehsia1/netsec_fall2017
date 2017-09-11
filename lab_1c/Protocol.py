import asyncio
import ../lab_1b/Packets
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

    def data_received(self, data):
        self.deserializer.update(data)
        packetCount += 1
        for packet in self.deserializer.nextPackets():
            if isinstance(packet, se)
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
