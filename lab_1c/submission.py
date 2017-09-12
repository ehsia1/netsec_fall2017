import Protocol
import Packets
from playground.network.testing import MockTransportToStorageStream, MockTransportToProtocol

def basicUnitTest():
    client = Protocol.ForgotPasswordClientProtocol()
    server = Protocol.ForgotPasswordServerProtocol()
    transportToClient = MockTransportToProtocol(client)
    transportToServer = MockTransportToProtocol(server)

    server.connection_made(transportToClient)
    client.connection_made(transportToServer)
    packet1 = Packets.RequestForgotPasswordPacket()
    packet1.userId = 'ehsia1'
    packet1Bytes = packet1.__serialize__()
    server.dataReceived(packet1Bytes)

if __name__ == "__main__":
    basicUnitTest()
