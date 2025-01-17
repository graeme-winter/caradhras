import os
import time
import zmq

host = "*"
port = 4242

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind(f"tcp://{host}:{port}")


def walker(directory="."):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.startswith("."):
                continue
            filename = os.path.join(root, file)
            print(filename)
            socket.send_multipart([filename.encode(), open(filename, "rb").read()])
            os.remove(filename)

while True:
    time.sleep(0.1)
    walker()
