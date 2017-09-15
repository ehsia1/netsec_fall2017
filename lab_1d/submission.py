import Protocol
import Packets
import playground
import asyncio
import sys
# from playground.network.testing import MockTransportToStorageStream, MockTransportToProtocol

def protocolController():
    loop = asyncio.get_event_loop()
    loop.set_debug(enabled=True)
    client = Protocol.ForgotPasswordClientProtocol()
    server = Protocol.ForgotPasswordServerProtocol()
    # cTransport, sTransport = MockTransportToProtocol.CreateTransportPair(client, server)
    # if sys.argv[1] == "server":
    serv = playground.getConnector().create_playground_server(lambda: server, 8080)
    s = loop.run_until_complete(serv)
    print("Echo server running at {}".format(s.sockets[0].gethostname()))
    # else:
    cli = playground.getConnector().create_playground_connection (lambda: client, "20174.1.1.1", 8080)
    transport, protocol = loop.run_until_complete(cli)
    print("Echo client running with t:{}. p:{}".format(transport, protocol))
    # server.connection_made(sTransport)
    # client.connection_made(cTransport)
    # client.send_initial_message()
    loop.run_forever()
    loop.close()

if __name__ == "__main__":
    protocolController()
