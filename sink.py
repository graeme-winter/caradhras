import os
import zmq

host = "i24-ppu01.diamond.ac.uk"
port = 4242

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect(f"tcp://{host}:{port}")

while 1:
    filename, content = socket.recv_multipart()
    if os.path.exists(filename):
        continue
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    with open(filename, "wb") as f:
        f.write(content)
    print(filename)
