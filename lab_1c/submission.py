import Protocol
import Packets
from playground.network.packet import PacketType
from playground.network.testing import MockTransportToStorageStream, MockTransportToProtocol

def basicUnitTest():
    client = Protocol.ForgotPasswordClientProtocol()
    server = Protocol.ForgotPasswordServerProtocol()
    cTransport, sTransport = MockTransportToProtocol.CreateTransportPair(client, server)

    server.connection_made(sTransport)
    client.connection_made(cTransport)
    # client.send_initial_message()

    packet1 = Packets.RequestForgotPasswordPacket()
    packet1.userId = 'ehsia1'
    packet1Bytes = packet1.__serialize__()
    sResponse1 = server.data_received(packet1Bytes)
    assert isinstance(sResponse1, Packets.SecurityQuestionPacket)
    packet2 = Packets.SecurityQuestionPacket()
    packet2.securityQuestion = 'What was your hometown?'
    packet2Bytes = packet2.__serialize__()
    cResponse1 = client.data_received(packet2Bytes)
    cResponse1 = PacketType.Deserialize(cResponse1)
    assert isinstance(cResponse1, Packets.SecurityAnswerPacket)
    packet3 = Packets.SecurityAnswerPacket()
    packet3.securityAnswer = 'Windsor, CT'
    packet3Bytes = packet3.__serialize__()
    sResponse2 = server.data_received(packet3Bytes)
    assert isinstance(sResponse2, Packets.ForgotPasswordTokenPacket)
    packet3.securityAnswer = 'Windsor'
    packet3Bytes = packet3.__serialize__()
    sResponse2 = server.data_received(packet3Bytes)
    assert sResponse2 == "Invalid"
    packet4 = Packets.ForgotPasswordTokenPacket()
    packet4.token = 'asdf2313241SqwerXq'
    packet4Bytes = packet4.__serialize__()
    cResponse2 = client.data_received(packet4Bytes)
    cResponse2 = PacketType.Deserialize(cResponse2)
    assert isinstance(cResponse2, Packets.ResetPasswordInputPacket)
    packet5 = Packets.ResetPasswordInputPacket()
    packet5.newPassword = 'gronkgronkgronk'
    packet5.passwordConfirmation = 'gronkgronkgronk'
    packet5Bytes = packet5.__serialize__()
    sResponse3 = server.data_received(packet5Bytes)
    assert isinstance(sResponse3, Packets.PasswordResetPacket)
    assert sResponse3.verification == True
    packet5.newPassword = 'gronkgronk'
    packet5.passwordConfirmation = 'gronkgronkgronk'
    packet5Bytes = packet5.__serialize__()
    sResponse3 = server.data_received(packet5Bytes)
    assert isinstance(sResponse3, Packets.PasswordResetPacket)
    assert sResponse3.verification == False

    print("Protocol completed! All tests passed!")
if __name__ == "__main__":
    basicUnitTest()
