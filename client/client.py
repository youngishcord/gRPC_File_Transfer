import grpc
import messages_pb2
import messages_pb2_grpc
from concurrent import futures
from config import (
    IP_PORT,
)


def run():
    with grpc.insecure_channel(IP_PORT) as channel:
        stub = messages_pb2_grpc.MessageStub(channel)

        with open('./storage/01_Баукова.zip', 'rb') as file:
            data = file.read()
            file_send = messages_pb2.FileUploadRequest(data=data)
            file.close()
        success_reply = stub.UploadFile(file_send)
        print(success_reply)

    return None


if __name__ == '__main__':
    run()