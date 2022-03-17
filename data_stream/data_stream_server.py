import random

import grpc
from concurrent import futures
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
import time
import data_stream_pb2_grpc as pb2_grpc
import data_stream_pb2 as pb2

SERVER_ID = 1


class DataStreamService(pb2_grpc.DataStreamServicer):

    def __init__(self, *args, **kwargs):
        pass

    def DataStreamingService(self, request, context):
        print("DataStreamingService called by client %d", request.client_id)

        # create a generator
        def response_messages():
            with open("traffic_violations.csv") as file:
                for line in file:
                    # Getting the current date and time
                    t = datetime.now().timestamp()
                    seconds = int(t)
                    nanos = int(t % 1 * 1e9)
                    timestamp = Timestamp(seconds=seconds, nanos=nanos)
                    response = pb2.DataResponse(
                        server_id=SERVER_ID,
                        response_data=line,
                        timestamp=timestamp
                    )
                    # sleep for a random time between 0 and .5 seconds
                    t = random.uniform(0, 0.5)
                    time.sleep(t)
                    time.sleep(0.01)
                    yield response

        return response_messages()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_DataStreamServicer_to_server(DataStreamService(), server)
    server.add_insecure_port('data_stream:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
