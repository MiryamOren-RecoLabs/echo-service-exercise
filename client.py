from __future__ import print_function
import logging

import grpc

import echo_pb2
import echo_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # # of the code.

    channel = grpc.insecure_channel('localhost:50051')
    stub = echo_pb2_grpc.EchoStub(channel)
    response = stub.Echo(echo_pb2.EchoRequest(word='thisIsMyRequestMessage!'))
    print('Call Echo, client received: ' + response.message)
    response = stub.EchoMany(echo_pb2.EchoRequest(word='thisIsMyRequestMessage!', repetitionNum=5))
    print('Call EchoMany, client received: ' + response.message)

if __name__ == '__main__':
    logging.basicConfig()
    run()
