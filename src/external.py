import concurrent.futures as futures
import grpc
import grpc_reflection.v1alpha.reflection as grpc_reflection
import logging
import image_generic_pb2
import image_generic_pb2_grpc

def calling_function(image):
    x=image
    return x

