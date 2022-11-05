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

    def UploadFile(self, request, context):
        print('[x] File upload called')
        success_reply = messages_pb2.FileSuccessReply()

        with open('./storage/01_Баукова.zip', 'wb') as file:
            file.write(request.data)
        
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