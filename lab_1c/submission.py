import Protocol
import Packets
from playground.network.testing import MockTransportToStorageStream, MockTransportToProtocol

def basicUnitTest():
    client = Protocol.ForgotPasswordClientProtocol()
    server = Protocol.ForgotPasswordServerProtocol()
    cTransport, sTransport = MockTransportToProtocol.CreateTransportPair(client, server)

    server.connection_made(sTransport)
    client.connection_made(cTransport)
    client.send_initial_message()

    # packet1 = Packets.RequestForgotPasswordPacket()
    # packet1.userId = 'ehsia1'
    # packet1Bytes = packet1.__serialize__()
    # sResponse1 = server.data_received(packet1Bytes)
    # assert isinstance(packet2, Packets.SecurityQuestionPacket)

    print("Protocol completed!")
if __name__ == "__main__":
    basicUnitTest()
