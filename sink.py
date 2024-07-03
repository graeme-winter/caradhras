import os
import zmq
import sys

port = 4242

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect(f"tcp://{sys.argv[1]}:{port}")

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
