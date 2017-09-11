import Protocol
from playground.network.testing import MockTransportToStorageStream, MockTransportToProtocol

def basicUnitTest():
    client = Protocol.ForgotPasswordClientProtocol()
    server = Protocol.ForgotPasswordServerProtocol()
    transportToClient = MockTransportToProtocol(client)
    transportToServer = MockTransportToProtocol(server)

    server.connection_made(transportToClient)
    client.connection_made(transportToServer)

if __name__ == "__main__":
    basicUnitTest()
