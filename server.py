from concurrent import futures
import logging

import grpc

import echo_pb2
import echo_pb2_grpc


class Echo(echo_pb2_grpc.EchoServicer):
    def Echo(self, request, context):
        return echo_pb2.EchoReplay(message=2*request.word)
    def EchoMany(self, request, context):
        return echo_pb2.EchoReplay(message=request.repetitionNum*request.word)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    echo_pb2_grpc.add_EchoServicer_to_server(Echo(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
