# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import llama_service_pb2 as llama__service__pb2

GRPC_GENERATED_VERSION = '1.66.2'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in llama_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class LlamaServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ProcessMessage = channel.unary_unary(
                '/llama_service.LlamaService/ProcessMessage',
                request_serializer=llama__service__pb2.MessageRequest.SerializeToString,
                response_deserializer=llama__service__pb2.MessageResponse.FromString,
                _registered_method=True)


class LlamaServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ProcessMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LlamaServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ProcessMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.ProcessMessage,
                    request_deserializer=llama__service__pb2.MessageRequest.FromString,
                    response_serializer=llama__service__pb2.MessageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'llama_service.LlamaService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('llama_service.LlamaService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class LlamaService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ProcessMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/llama_service.LlamaService/ProcessMessage',
            llama__service__pb2.MessageRequest.SerializeToString,
            llama__service__pb2.MessageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
