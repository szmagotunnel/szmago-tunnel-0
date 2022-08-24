import socket
import sys

class Niggrelel:

    def __init__(self, port):
        self.s = socket.socket()
        self.s.bind(('0.0.0.0', port))
        self.s.listen(5)

    def accept(self):
        c, addr = self.s.accept()
        print(addr)
        c.send(b'LMAO\n')
        c.close()

    def loop(self):
        while 1:
            self.accept()

port = int(sys.argv[1])
print(port, 'xd')
n = Niggrelel(port)
n.loop()
