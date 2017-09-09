import Packets

def basicUnitTest():
    # Forgot Password Request test
    packet1 = Packets.RequestForgotPasswordPacket()
    packet1Bytes = packet1._serialize_()
    packet1Test = Packets.RequestForgotPasswordPacket.Deserialize(packet1Bytes)
    assert packet1 == packet1Test

    packet2 = Packets.SecurityQuestionPacket()
    packet2Bytes = packet2._serialize_()
    packet2Test = Packets.SecurityQuestionPacket.Deserialize(packet2Bytes)
    assert packet2 == packet2Test

    packet3 = Packets.SecurityAnswerPacket()
    packet3Bytes = packet3._serialize_()
    packet3Test = Packets.SecurityAnswerPacket.Deserialize(packet3Bytes)
    assert packet4 == packet3Test

    packet4 = Packets.ForgotPasswordTokenPacket()
    packet4Bytes = packet4._serialize_()
    packet4Test = Packets.ForgotPasswordTokenPacket.Deserialize(packet4Bytes)
    assert packet4 == packet4Test

    packet5 = Packets.ResetPasswordInputPacket()
    packet5Bytes = packet5._serialize_()
    packet5Test = Packets.ResetPasswordInputPacket.Deserialize(packet5Bytes)
    assert packet5 == packet5Test

    packet6 = Packets.PasswordResetPacket()
    packet6Bytes = packet6._serialize_()
    packet6Test = Packets.PasswordResetPacket.Deserialize(packet6Bytes)
    assert packet6 == packet6Test
