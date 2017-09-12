import asyncio
import Packets
from playground.network.packet import PacketType

Protocol = asyncio.Protocol

class ForgotPasswordServerProtocol(Protocol):
    def __init__(self):
        self.transport = None
        self.deserializer = PacketType.Deserializer()

    def connection_made(self, transport):
        print("Echo server connected to client.")
        self.transport = transport

    def data_received(self, data):
        print("Receiving packet")
        self.deserializer.update(data)
        packet = PacketType.Deserialize(data)
        if isinstance(packet, Packets.RequestForgotPasswordPacket):
            packet2 = Packets.SecurityQuestionPacket()
            packet2.securityQuestion = 'What was your hometown?'
            packet2Bytes = packet2.__serialize__()
            self.transport.write(packet2Bytes)
        elif isinstance(packet, Packets.SecurityAnswerPacket):
            packet4 = Packets.ForgotPasswordTokenPacket()
            packet4.token = 'asdf2313241SqwerXq'
            packet4Bytes = packet4.__serialize__()
            self.transport.write(packet4Bytes)
        elif isinstance(packet, Packets.ResetPasswordInputPacket):
            packet6 = Packets.PasswordResetPacket()
            if packet.newPassword == packet.passwordConfirmation:
                packet6.verification = True
            else:
                packet6.verification = False
            packet6Bytes = packet6.__serialize__()
            self.transport.write(data)
        else:
            print("Packet was not recognized by server. Closing socket")
            self.transport.close()

    def connection_lost(self):
        print("Echo server connection lost because packet was not recognized")
        self.transport = None

class ForgotPasswordClientProtocol(Protocol):
    def __init__(self):
        self.transport = None
        self.deserializer = PacketType.Deserializer()

    def connection_made(self, transport):
        print("Echo client connected to server.")
        self.transport = transport
        packet1 = Packets.RequestForgotPasswordPacket()
        packet1.userId = 'ehsia1'
        packet1Bytes = packet1.__serialize__()
        self.transport.write(packet1Bytes)

    def data_received(self, data):
        print("Receiving packet")
        self.deserializer.update(data)
        packet = PacketType.Deserialize(data)
        if isinstance(packet, Packets.SecurityQuestionPacket):
            packet3 = Packets.SecurityAnswerPacket()
            packet3.securityAnswer = 'Windsor, CT'
            packet3Bytes = packet3.__serialize__()
            self.transport.write(packet3Bytes)
        elif isinstance(packet, Packets.ForgotPasswordTokenPacket):
            packet5 = Packets.ResetPasswordInputPacket()
            packet5.newPassword = 'gronkgronkgronk'
            packet5.passwordConfirmation = 'gronkgronkgronk'
            packet5Bytes = packet5.__serialize__()
            self.transport.write(packet5Bytes)
        elif isinstance(packet, Packets.PasswordResetPacket):
            if packet.verification == True:
                print("Password Reset!")
            else:
                print("Password Reset Failed!")
        else:
            print("Packet was not recognized by client. Closing socket")
            self.transport.close()

    def connection_lost(self):
        print("Echo client connection lost because packet was not recognized")
        self.transport = None
