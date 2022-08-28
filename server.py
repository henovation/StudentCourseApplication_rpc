from concurrent.futures import ThreadPoolExecutor
from concurrent.futures.process import _threads_wakeups
from http.client import REQUEST_URI_TOO_LONG
import json
from subprocess import SubprocessError
from google.protobuf.json_format import MessageToJson
from google.protobuf.timestamp_pb2 import Timestamp


import grpc
from grpc_reflection.v1alpha import reflection
import logging
import redis
import scapp_pb2 as pb
import scapp_pb2_grpc as rpc
from student_service_helper import get_student_id, store_student, get_student_by_id
from course_service_helper import generate_course_id, store_course, get_course_by_id
from datetime import datetime


class StudentServices(rpc.StudentServicesServicer):
    def CreateStudent(self, request, context):
        try:
            new_student_id = get_student_id()
            timestamp = Timestamp()
            timestamp.GetCurrentTime()
            new_student = pb.Student(
                student_id=new_student_id,
                student_name=request.student_name,
                email=request.email,
                credit_capacity=36,
                create_student_datetime=timestamp,
            )
            store_student(new_student)
            success = True
        except:
            print('Something wrong when creating student')
            success = False
        return pb.CreateStudentResponse(success=success)

    def UpdateStudent(self, request, context):
        try:
            student = get_student_by_id(request.student_id)
            updated_student = pb.Student(
                student_id=request.student_id,
                student_name=request.student_name,
                email=request.email,
            )
            print("Updated info: ", updated_student)
            success = True
        except:
            print('Something wrong when updating')
            success = False
        return pb.UpdateStudentResponse(success=success)

    def GetCourse(self, request, context):
        student = get_student_by_id(request.student_id)
        return pb.GetCoursesResponse(course_list=student.registered_courses_id)

class CourseServcies(rpc.CourseServicesServicer):
    def CreateCourse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        try:
            new_course_id = generate_course_id()
            print(new_course_id)
            timestamp = Timestamp()
            timestamp.GetCurrentTime()
            new_course = pb.Course(
                course_id=new_course_id,
                course_name=request.course_name,
                credits=request.credits,
                start_date=request.start_date,
                end_date=request.end_date,
                scheduled_course_time=request.scheduled_course_time,
            )
            store_course(new_course)
            success = True
        except:
            print('Something wrong when creating course')
            success = False
        return pb.CreateCourseResponse(success=success)

    def UpdateCourse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddStudent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveStudent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CalculateAve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStudent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStudentGrade(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetCourseData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

if __name__ == '__main__':
    import config

    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    rpc.add_StudentServicesServicer_to_server(StudentServices(), server)
    rpc.add_CourseServicesServicer_to_server(CourseServcies(), server)


    addr = f'[::]:{config.port}'
    server.add_insecure_port(addr)
    server.start()

    print('server ready on %s', addr)
    server.wait_for_termination()