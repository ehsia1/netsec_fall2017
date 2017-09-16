import Protocol
import playground
from playground.network.common import StackingProtocol

class PassThrough1(StackingProtocol):
    def __init__(self):
        self.transport = None
        self.count = 0

    def setHigherProtocol(self, higherProtocol):
        self._higherProtocol = higherProtocol
        if self.count == 0:
            self._higherProtocol.connection_made()
            print("Connection made.")
        elif self.count < 3:
            self._higherProtocol.data_received()
        else:
            self.connection_lost()
        self.count += 1

class PassThrough2(StackingProtocol):
    def __init__(self):
        self.transport = None

    def setHigherProtocol(self, higherProtocol):
        self._higherProtocol = higherProtocol
        if self.count == 0:
            self._higherProtocol.connection_made()
            print("Connection made.")
        elif self.count < 3:
            self._higherProtocol.data_received()
        else:
            self.connection_lost()
        self.count += 1
