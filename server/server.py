import grpc
import messages_pb2
import messages_pb2_grpc
from concurrent import futures
from config import (
    IP_PORT,
)


class MessageServicer(messages_pb2_grpc.MessageServicer):

    def CommandMessage(self, request, context):
        return super().CommandMessage(request, context)

    def UploadFile(self, request_iterator, context):
        print('[x] File upload called')
        arr = []
        for request in request_iterator:
            arr.append(request.data)

        f = b''.join(arr)

        with open('./storage/01_Баукова.zip', 'wb') as file:
            file.write(f)

        success_reply = messages_pb2.FileSuccessReply()
        success_reply.success = 'SUCCESS'
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