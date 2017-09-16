import Protocol
import playground
from playground.network.common import StackingProtocol

class PassThrough1(StackingProtocol):
    def __init__(self):
        self.transport = None

class PassThrough2(StackingProtocol):
    def __init__(self):
        self.transport = None
