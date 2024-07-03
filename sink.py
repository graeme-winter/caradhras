import os
import zmq

host = "ws448.diamond.ac.uk"
port = 4242

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect(f"tcp://{host}:{port}")

while 1:
    filename, content = socket.recv_multipart()
    if os.path.exists(filename):
        continue
    if not os.path.exists(os.dirname(filename)):
        os.makedirs(os.dirname(filename))
    with open(filename, "wb") as f:
        f.write(content)
    print(filename)