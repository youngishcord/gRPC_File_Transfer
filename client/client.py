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


def get_name(path: str) -> str:
    if '\\' in path:
        return path.split('\\')[-1]
    elif '/' in path:
        return path.split('/')[-1]


def read_file(path):
    metadata = messages_pb2.MetaData(
        file_name=get_name(path),
        md5=md5(path),
        backup=True,
    )
    yield messages_pb2.FileUploadRequest(metadata=metadata)

    with open(path, "rb") as file:
        while True:
            chunk = file.read(1024)
            if chunk:
                entry_request = messages_pb2.FileUploadRequest(chunk=chunk)
                yield entry_request
            else:
                return


def run(path):
    with grpc.insecure_channel(IP_PORT) as channel:
        stub = messages_pb2_grpc.MessageStub(channel)

        response = stub.UploadFile(read_file(path))
        print(response)

    return None


if __name__ == '__main__':
    run("./storage/01_Баукова.zip") # 02_Гаврилов 01_Баукова