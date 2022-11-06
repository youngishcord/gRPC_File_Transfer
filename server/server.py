import grpc
import hashlib
import messages_pb2
import messages_pb2_grpc
from concurrent import futures
from config import (
    IP_PORT,
)


def md5(path: str) -> str:
    hash_md5 = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


class MessageServicer(messages_pb2_grpc.MessageServicer):

    def UploadFile(self, request_iterator, context):
        print('[x] File upload called')

        data = bytearray()
        for request in request_iterator:
            if request.metadata.md5:
                file_path = f'./storage/{request.metadata.file_name}'
                file_md5 = request.metadata.md5
                backup = request.metadata.backup
                continue
            data.extend(request.chunk)

        with open(file_path, 'wb') as file:
            file.write(data)
        
        success_reply = messages_pb2.FileSuccessReply()
        # print(file_md5)
        # print(md5(file_path))
        if md5(file_path) == file_md5:
            success_reply.status = 1
        else:
            success_reply.status = 2
        return success_reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    messages_pb2_grpc.add_MessageServicer_to_server(MessageServicer(), server)
    server.add_insecure_port(IP_PORT)

    print('[x] Server started')

    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()