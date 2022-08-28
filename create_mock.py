import pandas as pd
import scapp_pb2 as pb
import scapp_pb2_grpc as rpc
import grpc
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp



def create_mock_students(df):
    for i in range(len(df)):
        with grpc.insecure_channel('localhost:1024') as channel:
            stub = rpc.StudentServicesStub(channel)
            response = stub.CreateStudent(pb.CreateStudentRequest(student_name=df.loc[i, 'name'], email=df.loc[i, 'email']))

def create_mock_courses(df):
    for i in range(len(df)):
        start_date = courses_df.loc[i, 'start_date']
        st_dl = start_date.split('-')
        st_dt = datetime(int(st_dl[0]), int(st_dl[1]), int(st_dl[2]))
        st_timestamp = Timestamp()
        st_timestamp.FromDatetime(st_dt)
        
        end_date = courses_df.loc[i, 'end_date']
        end_dl = end_date.split('-')
        end_dt = datetime(int(end_dl[0]), int(end_dl[1]), int(end_dl[2]))
        end_timestamp = Timestamp()
        end_timestamp.FromDatetime(end_dt)
        with grpc.insecure_channel('localhost:1024') as channel:
            stub = rpc.CourseServicesStub(channel)
            response = stub.CreateCourse(pb.CreateCourseRequest(course_name=df.loc[i, 'course_name'],credits=df.loc[i, 'credits'], start_date=st_timestamp, end_date=end_timestamp, scheduled_course_time=df.loc[i, 'scheduled_course_time']))


# if __name__ == "__main__":
    
    # students_df = pd.read_csv('mock_data/mock_students_data.csv')
    # create_mock_students(students_df)

    # courses_df = pd.read_csv('mock_data/mock_courses_data.csv')
    # create_mock_courses(courses_df)