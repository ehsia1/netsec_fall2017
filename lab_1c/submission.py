import asyncio
import Protocol
from playground.asyncio_lib.testing import TestLoopEx
from playground.network.testing import MockTransportToStorageStream, MockTransportToProtocol

def basicUnitTest():
    asyncio.set_event_loop(TestLoopEx())
    client = Protocol.ForgotPasswordClientProtocol()
    server = Protocol.ForgotPasswordServerProtocol()
    transportToClient = MockTransportToProtocol(client)
    transportToServer = MockTransportToProtocol(server)

    server.connection_made(transportToClient)
    client.connection_made(transportToServer)

if __name__ == "__main__":
    basicUnitTest()
