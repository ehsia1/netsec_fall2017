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
                print("Passwords matched!")
                packet6.verification = True
            else:
                print("Passwords did not match!")
                packet6.verification = False
            packet6Bytes = packet6.__serialize__()
            self.transport.write(packet6Bytes)
        else:
            print("Packet was not recognized by server. Closing socket")
            self.transport.close()

    def connection_lost(self):
        print("Echo server connection lost")
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
        def clientInput(packet):
            if isinstance(packet, Packets.SecurityQuestionPacket):
                packet3 = Packets.SecurityAnswerPacket()
                packet3.securityAnswer = input("Input answer to security question: ")
                packet3Bytes = packet3.__serialize__()
                return packet3Bytes
            elif isinstance(packet, Packets.ForgotPasswordTokenPacket):
                packet5 = Packets.ResetPasswordInputPacket()
                packet5.newPassword = input("Enter your new password: ")
                packet5.passwordConfirmation = input("Enter password again: ")
                packet5Bytes = packet5.__serialize__()
                return packet5Bytes
        print("Receiving packet")
        self.deserializer.update(data)
        packet = PacketType.Deserialize(data)
        if isinstance(packet, Packets.SecurityQuestionPacket):
            response = clientInput(packet)
            self.transport.write(response)
        elif isinstance(packet, Packets.ForgotPasswordTokenPacket):
            response = clientInput(packet)
            self.transport.write(response)
        elif isinstance(packet, Packets.PasswordResetPacket):
            if packet.verification == True:
                print("Password Reset!")
            else:
                print("Password Reset Failed!")
            self.transport.close()
        else:
            print("Packet was not recognized by client. Closing socket")
            self.transport.close()

    def connection_lost(self, exc):
        print("Echo client connection lost")
        self.transport = None
