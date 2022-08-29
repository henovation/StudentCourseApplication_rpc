import pandas as pd
import scapp_pb2 as pb
import scapp_pb2_grpc as rpc
import grpc
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp



def create_mock_students(df):
    for i in range(3):
        with grpc.insecure_channel('localhost:1024') as channel:
            stub = rpc.StudentServicesStub(channel)
            response = stub.CreateStudent(pb.CreateStudentRequest(student_name=df.loc[i, 'name'], email=df.loc[i, 'email']))

def create_mock_courses(df):
    for i in range(len(df)):       
        with grpc.insecure_channel('localhost:1024') as channel:
            stub = rpc.CourseServicesStub(channel)
            response = stub.CreateCourse(pb.CreateCourseRequest(course_name=df.loc[i, 'course_name'],credits=df.loc[i, 'credits'], start_date=df.loc[i, 'start_date'], end_date=df.loc[i, 'end_date'], course_schedule=df.loc[i, 'course_schedule']))


if __name__ == "__main__":
    
    students_df = pd.read_csv('mock_data/mock_students_data.csv')
    create_mock_students(students_df)

    courses_df = pd.read_csv('mock_data/mock_courses_data.csv')
    create_mock_courses(courses_df)