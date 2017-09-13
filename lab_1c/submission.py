import Protocol
import Packets
from playground.network.testing import MockTransportToStorageStream, MockTransportToProtocol

def basicUnitTest():
    client = Protocol.ForgotPasswordClientProtocol()
    server = Protocol.ForgotPasswordServerProtocol()
    transportToClient = MockTransportToProtocol(myProtocol=client)
    transportToServer = MockTransportToProtocol(myProtocol=server)
    transportToServer.setRemoteTransport(transportToClient)
    transportToClient.setRemoteTransport(transportToServer)

    server.connection_made(transportToClient)
    client.connection_made(transportToServer)

    print("Protocol completed!")
if __name__ == "__main__":
    basicUnitTest()
