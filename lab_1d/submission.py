import Protocol
import Packets
import playground
import asyncio

def protocolController():
    loop = asyncio.get_event_loop()
    loop.set_debug(enabled=True)
    client = Protocol.ForgotPasswordClientProtocol()
    server = Protocol.ForgotPasswordServerProtocol()
    serv = playground.getConnector().create_playground_server(lambda: server, 8080)
    s = loop.run_until_complete(serv)
    print("Echo server running at {}".format(s.sockets[0].gethostname()))
    cli = playground.getConnector().create_playground_connection (lambda: client, "20174.1.1.1", 8080)
    transport, protocol = loop.run_until_complete(cli)
    print("Echo client running with t:{}. p:{}".format(transport, protocol))
    loop.run_forever()
    loop.close()

if __name__ == "__main__":
    protocolController()
