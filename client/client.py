import grpc
import messages_pb2
import messages_pb2_grpc
from concurrent import futures
from config import (
    IP_PORT,
)


def read_file(path):
    with open("./storage/01_Баукова.zip", "rb") as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            file_send = messages_pb2.Chunk(data=data)
            yield file_send


def run():
    with grpc.insecure_channel(IP_PORT) as channel:
        stub = messages_pb2_grpc.MessageStub(channel)
        success_reply = stub.UploadFile(read_file('path'))
        print(success_reply)

    return None


if __name__ == '__main__':
    run()