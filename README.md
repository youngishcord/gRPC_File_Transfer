# gRPC_File_Transfer
---

py -m grpc_tools.protoc -I protos --python_out=./client/ --pyi_out=./client/ --grpc_python_out=./client/ protos/messages.proto

py -m grpc_tools.protoc -I protos --python_out=./server/ --pyi_out=./server/ --grpc_python_out=./server/ protos/messages.proto