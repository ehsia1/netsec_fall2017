import Protocol
import playground
from playground.network.common import StackingProtocol

class PassThrough1(StackingProtocol):
    def __init__(self):
        self.transport = None
        self.count = 0

    def setHigherProtocol(self, higherProtocol=Protocol.ForgotPasswordServerProtocol()):
        self._higherProtocol = higherProtocol
        if self.count == 0:
            self.higherProtocol().connection_made()
            print("Connection made.")
        elif self.count < 3:
            self.higherProtocol().data_received()
        else:
            self.higherProtocol().connection_lost()
        self.count += 1

class PassThrough2(StackingProtocol):
    def __init__(self):
        self.transport = None

    def setHigherProtocol(self, higherProtocol=Protocol.ForgotPasswordClientProtocol()):
        self._higherProtocol = higherProtocol
        if self.count == 0:
            self.higherProtocol().connection_made()
            print("Connection made.")
        elif self.count < 3:
            self.higherProtocol().data_received()
        else:
            self.higherProtocol().connection_lost()
        self.count += 1
