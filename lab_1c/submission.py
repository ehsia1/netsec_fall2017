import Protocol
import Packets
from playground.network.testing import MockTransportToStorageStream, MockTransportToProtocol

def basicUnitTest():
    client = Protocol.ForgotPasswordClientProtocol()
    server = Protocol.ForgotPasswordServerProtocol()
    transportToClient = MockTransportToProtocol(client)
    transportToServer = MockTransportToProtocol(server)

    server.connection_made(transportToClient)
    client.connection_made(transportToServer)
    packet1 = Packets.RequestForgotPasswordPacket()
    packet1.userId = 'ehsia1'
    packet1Bytes = packet1.__serialize__()
    packet2 = Packets.SecurityQuestionPacket()
    packet2.securityQuestion = 'What was your hometown?'
    packet2Bytes = packet2.__serialize__()
    packet3 = Packets.SecurityAnswerPacket()
    packet3.securityAnswer = 'Windsor, CT'
    packet3Bytes = packet3.__serialize__()
    packet4 = Packets.ForgotPasswordTokenPacket()
    packet4.token = 'asdf2313241SqwerXq'
    packet4Bytes = packet4.__serialize__()
    packet5 = Packets.ResetPasswordInputPacket()
    packet5.newPassword = 'gronkgronkgronk'
    packet5.passwordConfirmation = 'gronkgronkgronk'
    packet5Bytes = packet5.__serialize__()
    packet6 = Packets.PasswordResetPacket()
    packet6.verification = True
    packet6Bytes = packet6.__serialize__()
    packet7 = Packets.ResetPasswordInputPacket()
    packet7.newPassword = 'gronkgronkgronk'
    packet7.passwordConfirmation = 'gronkgronk'
    packet7Bytes = packet7.__serialize__()
    packet8 = Packets.PasswordResetPacket()
    packet8.verification = False
    packet8Bytes = packet8.__serialize__()
    server.data_received(packet1Bytes)
    client.data_received(packet2Bytes)
    server.data_received(packet3Bytes)
    client.data_received(packet4Bytes)
    server.data_received(packet5Bytes)
    client.data_received(packet6Bytes)

if __name__ == "__main__":
    basicUnitTest()
