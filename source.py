import os
import zmq

host = "*"
port = 4242

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind(f"tcp://{host}:{port}")


def walker(directory="."):
    for root, _, files in os.walk(directory):
        for file in files:
            filename = os.path.join(root, file)
            print(filename)
            socket.send_multipart([filename.encode(), open(filename, "rb").read()])


walker()
