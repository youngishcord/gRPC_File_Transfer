# gRPC_File_Transfer
---
## This is a simple example of a program for transferring a file via gRPC with pre-sending the file name and md5 summ.

Commands for creating protocol-scripts:

py -m grpc_tools.protoc -I protos --python_out=./client/ --pyi_out=./client/ --grpc_python_out=./client/ protos/messages.proto

py -m grpc_tools.protoc -I protos --python_out=./server/ --pyi_out=./server/ --grpc_python_out=./server/ protos/messages.proto

