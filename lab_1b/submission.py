import Packets

def basicUnitTest():
    # Forgot Password Request test
    packet1 = Packets.RequestForgotPasswordPacket()
    packet1Bytes = packet1._serialize_()
    packet1Test = Packets.RequestForgotPasswordPacket.Deserialize(packet1Bytes)
    assert packet1 == packet1Test
