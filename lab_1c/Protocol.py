import asyncio
import Packets
import re
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
        for packet in self.deserializer.nextPackets():
            if isinstance(packet, Packets.RequestForgotPasswordPacket):
                # Validation limited because there does not exist a database of valid userIds (same with security q/a)
                packet2 = Packets.SecurityQuestionPacket()
                packet2.securityQuestion = 'What was your hometown?'
                packet2Bytes = packet2.__serialize__()
                self.transport.write(packet2Bytes)
                # return packet2
            elif isinstance(packet, Packets.SecurityAnswerPacket):
                # Validate the answer of the hometown Security Question for format
                # Expecting format of {Town}, {stateAbbreviation} such as 'Windsor, CT'
                if re.match(r'(.*), [A-Z]{2}$', packet.securityAnswer, flags=0):
                    packet4 = Packets.ForgotPasswordTokenPacket()
                    packet4.token = 'asdf2313241SqwerXq'
                    packet4Bytes = packet4.__serialize__()
                    self.transport.write(packet4Bytes)
                else:
                    print("Answer was of invalid format, must be of form '[town], [stateAbbreviation]'")
                    self.transport.close()
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

    def connection_lost(self, exc):
        print("Echo server connection lost")
        self.transport = None

class ForgotPasswordClientProtocol(Protocol):
    def __init__(self):
        self.transport = None
        self.deserializer = PacketType.Deserializer()

    def connection_made(self, transport):
        print("Echo client connected to server.")
        self.transport = transport

    def send_initial_message(self):
        packet1 = Packets.RequestForgotPasswordPacket()
        message = self.clientInput(packet1)
        self.transport.write(message)

    def data_received(self, data):
        print("Receiving packet")
        self.deserializer.update(data)
        for packet in self.deserializer.nextPackets():
            if isinstance(packet, Packets.SecurityQuestionPacket):
                print(packet.securityQuestion)
                response = self.clientInput(packet)
                self.transport.write(response)
            elif isinstance(packet, Packets.ForgotPasswordTokenPacket):
                print("Security Question Correct, here's your token", packet.token)
                response = self.clientInput(packet)
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

    def clientInput(self, packet):
        if isinstance(packet, Packets.SecurityQuestionPacket):
            packetNew = Packets.SecurityAnswerPacket()
            packetNew.securityAnswer = input("Input answer to security question: ")
            packetNewBytes = packetNew.__serialize__()
            return packetNewBytes
        elif isinstance(packet, Packets.ForgotPasswordTokenPacket):
            packetNew = Packets.ResetPasswordInputPacket()
            packetNew.newPassword = input("Enter your new password: ")
            packetNew.passwordConfirmation = input("Enter password again: ")
            packetNewBytes = packetNew.__serialize__()
            return packetNewBytes
        elif isinstance(packet, Packets.RequestForgotPasswordPacket):
            packet.userId = input("Input username associated with account: ")
            packetBytes = packet.__serialize__()
            return packetBytes

    def connection_lost(self, exc):
        print("Echo client connection lost")
        self.transport = None
