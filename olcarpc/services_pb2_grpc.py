# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import olcarpc.olca_pb2 as olca__pb2
import olcarpc.services_pb2 as services__pb2


class DataServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.actors = channel.unary_stream(
                '/protolca.services.DataService/actors',
                request_serializer=services__pb2.Empty.SerializeToString,
                response_deserializer=olca__pb2.Actor.FromString,
                )
        self.actor = channel.unary_unary(
                '/protolca.services.DataService/actor',
                request_serializer=olca__pb2.Ref.SerializeToString,
                response_deserializer=olca__pb2.Actor.FromString,
                )
        self.put_actor = channel.unary_unary(
                '/protolca.services.DataService/put_actor',
                request_serializer=olca__pb2.Actor.SerializeToString,
                response_deserializer=olca__pb2.Ref.FromString,
                )
        self.flow = channel.unary_unary(
                '/protolca.services.DataService/flow',
                request_serializer=olca__pb2.Ref.SerializeToString,
                response_deserializer=olca__pb2.Flow.FromString,
                )
        self.put_flow = channel.unary_unary(
                '/protolca.services.DataService/put_flow',
                request_serializer=olca__pb2.Flow.SerializeToString,
                response_deserializer=olca__pb2.Ref.FromString,
                )


class DataServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def actors(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def actor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def put_actor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def flow(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def put_flow(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'actors': grpc.unary_stream_rpc_method_handler(
                    servicer.actors,
                    request_deserializer=services__pb2.Empty.FromString,
                    response_serializer=olca__pb2.Actor.SerializeToString,
            ),
            'actor': grpc.unary_unary_rpc_method_handler(
                    servicer.actor,
                    request_deserializer=olca__pb2.Ref.FromString,
                    response_serializer=olca__pb2.Actor.SerializeToString,
            ),
            'put_actor': grpc.unary_unary_rpc_method_handler(
                    servicer.put_actor,
                    request_deserializer=olca__pb2.Actor.FromString,
                    response_serializer=olca__pb2.Ref.SerializeToString,
            ),
            'flow': grpc.unary_unary_rpc_method_handler(
                    servicer.flow,
                    request_deserializer=olca__pb2.Ref.FromString,
                    response_serializer=olca__pb2.Flow.SerializeToString,
            ),
            'put_flow': grpc.unary_unary_rpc_method_handler(
                    servicer.put_flow,
                    request_deserializer=olca__pb2.Flow.FromString,
                    response_serializer=olca__pb2.Ref.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protolca.services.DataService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def actors(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/protolca.services.DataService/actors',
            services__pb2.Empty.SerializeToString,
            olca__pb2.Actor.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def actor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protolca.services.DataService/actor',
            olca__pb2.Ref.SerializeToString,
            olca__pb2.Actor.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def put_actor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protolca.services.DataService/put_actor',
            olca__pb2.Actor.SerializeToString,
            olca__pb2.Ref.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def flow(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protolca.services.DataService/flow',
            olca__pb2.Ref.SerializeToString,
            olca__pb2.Flow.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def put_flow(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protolca.services.DataService/put_flow',
            olca__pb2.Flow.SerializeToString,
            olca__pb2.Ref.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
