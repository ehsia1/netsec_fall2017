import Packets

def basicUnitTest():
    # Forgot Password Request test
    packet1 = Packets.RequestForgotPasswordPacket()
    packet1.userId = 'ehsia1'
    packet1Bytes = packet1._serialize_()
    packet1Test = Packets.RequestForgotPasswordPacket.Deserialize(packet1Bytes)
    assert packet1 == packet1Test

    packet2 = Packets.SecurityQuestionPacket()
    packet2.securityQuestion = 'What was your hometown?'
    packet2Bytes = packet2._serialize_()
    packet2Test = Packets.SecurityQuestionPacket.Deserialize(packet2Bytes)
    assert packet2 == packet2Test

    packet3 = Packets.SecurityAnswerPacket()
    packet3.securityAnswer = 'Windsor, CT'
    packet3Bytes = packet3._serialize_()
    packet3Test = Packets.SecurityAnswerPacket.Deserialize(packet3Bytes)
    assert packet3 == packet3Test

    packet4 = Packets.ForgotPasswordTokenPacket()
    packet4.token = 'asdf2313241SqwerXq'
    packet4Bytes = packet4._serialize_()
    packet4Test = Packets.ForgotPasswordTokenPacket.Deserialize(packet4Bytes)
    assert packet4 == packet4Test

    packet5 = Packets.ResetPasswordInputPacket()
    packet5.newPassword = 'gronkgronkgronk'
    packet5.passwordConfirmation = 'gronkgronkgronk'
    packet5Bytes = packet5._serialize_()
    packet5Test = Packets.ResetPasswordInputPacket.Deserialize(packet5Bytes)
    assert packet5 == packet5Test

    packet6 = Packets.PasswordResetPacket()
    packet6.verification = True
    packet6Bytes = packet6._serialize_()
    packet6Test = Packets.PasswordResetPacket.Deserialize(packet6Bytes)
    assert packet6 == packet6Test

    packet7 = Packets.ResetPasswordInputPacket()
    packet7.newPassword = 'gronkgronkgronk'
    packet7.passwordConfirmation = 'gronkgronk'
    packet7Bytes = packet7._serialize_()
    packet7Test = Packets.ResetPasswordInputPacket.Deserialize(packet7Bytes)
    assert packet7 == packet7Test

    packet8 = Packets.PasswordResetPacket()
    packet8.verification = False
    packet8Bytes = packet8._serialize_()
    packet8Test = Packets.PasswordResetPacket.Deserialize(packet8Bytes)
    assert packet8 == packet8Test
