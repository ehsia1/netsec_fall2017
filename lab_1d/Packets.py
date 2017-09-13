from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import STRING, BOOL

class RequestForgotPasswordPacket (PacketType):
    DEFINITION_IDENTIFIER = "lab1b.ehsia1.RequestForgotPasswordPacket"
    DEFINITION_VERSION = "1.0"

    FIELDS = [
        ("userId", STRING)
    ]

class SecurityQuestionPacket (PacketType):
    DEFINITION_IDENTIFIER = "lab1b.ehsia1.SecurityQuestionPacket"
    DEFINITION_VERSION = "1.1"

    FIELDS = [
        ("securityQuestion", STRING)
    ]

class SecurityAnswerPacket (PacketType):
    DEFINITION_IDENTIFIER = "lab1b.ehsia1.SecurityAnswerPacket"
    DEFINITION_VERSION = "1.2"

    FIELDS = [
        ("securityAnswer", STRING)
    ]

class ForgotPasswordTokenPacket (PacketType):
    DEFINITION_IDENTIFIER = "lab1b.ehsia1.ForgotPasswordTokenPacket"
    DEFINITION_VERSION = "1.3"

    FIELDS = [
        ("token", STRING)
    ]

class ResetPasswordInputPacket (PacketType):
    DEFINITION_IDENTIFIER = "lab1b.ehsia1.ResetPasswordInputPacket"
    DEFINITION_VERSION = "1.4"

    FIELDS = [
        ("newPassword", STRING),
        ("passwordConfirmation", STRING)
    ]

class PasswordResetPacket (PacketType):
    DEFINITION_IDENTIFIER = "lab1b.ehsia1.PasswordResetPacket"
    DEFINITION_VERSION = "1.5"

    FIELDS = [
        ("verification", BOOL)
    ]
