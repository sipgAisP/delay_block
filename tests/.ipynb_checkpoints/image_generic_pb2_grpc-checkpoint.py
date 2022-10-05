# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import image_generic_pb2 as image__generic__pb2


class ImageGenericServiceStub(object):
    """
    Service that receives an image, applies some
    transformation to it and returns the new image
    :param Image: The image to process
    :returns: The transformed image
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.process = channel.unary_unary(
                '/ImageGenericService/process',
                request_serializer=image__generic__pb2.Image.SerializeToString,
                response_deserializer=image__generic__pb2.Image.FromString,
                )


class ImageGenericServiceServicer(object):
    """
    Service that receives an image, applies some
    transformation to it and returns the new image
    :param Image: The image to process
    :returns: The transformed image
    """

    def process(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ImageGenericServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'process': grpc.unary_unary_rpc_method_handler(
                    servicer.process,
                    request_deserializer=image__generic__pb2.Image.FromString,
                    response_serializer=image__generic__pb2.Image.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ImageGenericService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ImageGenericService(object):
    """
    Service that receives an image, applies some
    transformation to it and returns the new image
    :param Image: The image to process
    :returns: The transformed image
    """

    @staticmethod
    def process(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ImageGenericService/process',
            image__generic__pb2.Image.SerializeToString,
            image__generic__pb2.Image.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)