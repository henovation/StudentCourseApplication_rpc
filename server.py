from concurrent.futures import ThreadPoolExecutor
from concurrent.futures.process import _threads_wakeups
from http.client import REQUEST_URI_TOO_LONG
import json
from subprocess import SubprocessError
from uuid import uuid4
from google.protobuf.json_format import MessageToJson

import grpc
from grpc_reflection.v1alpha import reflection
import logging
import redis
import assignments_pb2 as pb
import assignments_pb2_grpc as rpc

r = redis.Redis(
    host='localhost',
    port=6379)


def generate_student_id():
    return uuid4().int

def new_course_id():
    return uuid4().hex


class Students(rpc.StudentsServicer):
    def Create(self, request, context):
        try:
            new_student_id = generate_student_id()
            print("Original Proto Request:", request)

            data = request.SerializeToString()
            print("StringBytes data:", data)
            r.set(new_student_id, data)
            success = True
        except:
            success = False
        return pb.CreateStudentResponse(success=success)

    def Update(self, request, context):
        try:
            print('/n/n/nUpdating request:', request)
            print(type(request.student_id))
            data = request.SerializeToString()
            success = True
        except:
            print('Something wrong when updating')
            success = False
        return pb.UpdateStudentResponse(success=success)


if __name__ == '__main__':
    import config

    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    rpc.add_StudentsServicer_to_server(Students(), server)

    addr = f'[::]:{config.port}'
    server.add_insecure_port(addr)
    server.start()

    print('server ready on %s', addr)
    server.wait_for_termination()