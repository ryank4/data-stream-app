# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import data_stream_pb2 as data__stream__pb2


class DataStreamStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DataStreamingService = channel.unary_stream(
                '/data_stream.DataStream/DataStreamingService',
                request_serializer=data__stream__pb2.Data.SerializeToString,
                response_deserializer=data__stream__pb2.DataResponse.FromString,
                )


class DataStreamServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DataStreamingService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataStreamServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DataStreamingService': grpc.unary_stream_rpc_method_handler(
                    servicer.DataStreamingService,
                    request_deserializer=data__stream__pb2.Data.FromString,
                    response_serializer=data__stream__pb2.DataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'data_stream.DataStream', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataStream(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DataStreamingService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/data_stream.DataStream/DataStreamingService',
            data__stream__pb2.Data.SerializeToString,
            data__stream__pb2.DataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
