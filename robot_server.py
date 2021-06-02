import socketserver
from  ev3dev2.motor  import  OUTPUT_C , OUTPUT_B , LargeMotor

class Handler_TCPServer(socketserver.BaseRequestHandler):

    def executer_commande(self,msg):
        lmotor , rmotor = [LargeMotor(address) for  address  in (OUTPUT_C , OUTPUT_B)]
        print(msg)
        # just send back ACK for data arrival confirmation
        self.request.sendall("ACK from TCP Server".encode())

        if msg[:4]==(b"MOVE"):
            commandes=msg[5:].split(b" ")
            print(commandes)
            rmotor.stop()
            lmotor.stop()
            rmotor.run_forever(speed_sp=int(commandes[0]))
            lmotor.run_forever(speed_sp=int(commandes[1]))

        elif msg==(b"STOP"):
            rmotor.stop()
            lmotor.stop()


    def handle(self):
        while 1:
            # self.request - TCP socket connected to the client
            data = self.request.recv(1024)
            if not data:
                break
            data.strip()
            print("{} sent:".format(self.client_address[0]))
            self.executer_commande(data)

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999

    # Init the TCP server object, bind it to the localhost on 9999 port
    tcp_server = socketserver.TCPServer((HOST, PORT), Handler_TCPServer)

    # Activate the TCP server.
    # To abort the TCP server, press Ctrl-C.
    tcp_server.serve_forever()