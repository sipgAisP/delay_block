import concurrent.futures as futures
import grpc
import grpc_reflection.v1alpha.reflection as grpc_reflection
import logging
import image_generic_pb2
import image_generic_pb2_grpc
import utils


class ServiceImpl(image_generic_pb2_grpc.ImageGenericServiceServicer):

    def __init__(self, calling_function):
        """
        Args:
            calling_function: the function that should be called
                              when a new request is received

                              the signature of the function should be:

                              (image: bytes) -> bytes

                              as described in the process method

        """
        self.__calling_fn = calling_function
        self.isfirst=1



    def process(self, request: image_generic_pb2.Image, context):
        """Processes a given ImageWithPoses request

        It expects that a process function was already registered
        with the following signature

        (image: bytes) -> bytes

        Image is the bytes of the image to process.

        Args:
            request: The ImageWithPoses request to process
            context: Context of the gRPC call

        Returns:
            The Image with the applied function

        """
        if self.isfirst ==1 :
            self.isfirst = 0
            image = request.data
            self.previousim = image
            processed_image = image #na primeira vez retorna a propria img
        else :
            image = request.data
            processed_image = self.previousim #devia ser self.__calling_fn(image)
            self.previousim = image
        return image_generic_pb2.Image(data=processed_image)


if __name__ == '__main__':
    logging.basicConfig(
        format='[ %(levelname)s ] %(asctime)s (%(module)s) %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.INFO)

    calling_fn = utils.get_calling_function()
    if not calling_fn:
        exit(1)

    server = grpc.server(futures.ThreadPoolExecutor())
    image_generic_pb2_grpc.add_ImageGenericServiceServicer_to_server(
        ServiceImpl(calling_fn),
        server)

    # Add reflection
    service_names = (
        image_generic_pb2.DESCRIPTOR.services_by_name['ImageGenericService'].full_name,
        grpc_reflection.SERVICE_NAME
    )
    grpc_reflection.enable_server_reflection(service_names, server)

    utils.run_server(server)
