import Protocol
import Packets
import playground

def protocolController():
    client = Protocol.ForgotPasswordClientProtocol()
    server = Protocol.ForgotPasswordServerProtocol()
    playground.getConnector().create_playground_server(server, 2020)
    playground.getConnector().create_playground_connection(client, 20174.0.0.1 ,2020)

if __name__ == "__main__":
    protocolController()
