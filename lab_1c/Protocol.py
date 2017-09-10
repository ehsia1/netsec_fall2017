import asyncio
from playground.asyncio_lib.testing import TestLoopEx
from playground.network.testing import MockTransportToStorageStream, MockTransportToProtocol

Protocol = asyncio.Protocol

class ForgotPasswordProtocol(Protocol):
    def __init__(self):
        self.transport = None

    def connection_made(self, transport):
        print("Echo server connected to client.")
        self.transport = transport

    def data_received(self, data):
        self.transport.write(data)

    def connection_lost(self, exc):
        print("Echo server connection lost because {}".format(exc))
