import Protocol
import playground
from playground.network.common import StackingProtocol, StackingTransport

class PassThrough1(StackingProtocol):
    def __init__(self):
        self.transport = None
        self.count = 0

    def connection_made(self, transport):
        self.transport = transport
        self.higherProtocol().connection_made(StackingTransport(transport))
        print("Connection Made to Server")

    def data_received(self, data):
        self.higherProtocol().data_received(data)
        print("Write got {} bytes of data to pass to lower layer".format(len(data)))

class PassThrough2(StackingProtocol):
    def __init__(self):
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport
        print("Connection made to Client")
        self.higherProtocol().connection_made(StackingTransport(transport))

    def data_received(self, data):
        self.higherProtocol().data_received(data)
        print("Write got {} bytes of data to pass to lower layer".format(len(data)))
