import grpc
import pandas as pd
import grpc_app.helper.generated.scapp_pb2 as pb
import grpc_app.helper.generated.scapp_pb2_grpc as rpc
from grpc_app.helper.utils import db


def create_mock_students(df):
    for i in range(3):
        with grpc.insecure_channel('localhost:1024') as channel:
            stub = rpc.StudentServicesStub(channel)
            response = stub.CreateStudent(pb.CreateStudentRequest(student_name=df.loc[i, 'name'], email=df.loc[i, 'email']))
            print('Creating Student {}\'s profile result. {}'.format(df.loc[i, 'name'], response))

def create_mock_courses(df):
    for i in range(len(df)):       
        with grpc.insecure_channel('localhost:1024') as channel:
            stub = rpc.CourseServicesStub(channel)
            response = stub.CreateCourse(pb.CreateCourseRequest(course_name=df.loc[i, 'course_name'],credits=df.loc[i, 'credits'], start_date=df.loc[i, 'start_date'], end_date=df.loc[i, 'end_date'], course_schedule=df.loc[i, 'course_schedule']))
            print('Creating Course {}\'s content result. {}'.format(df.loc[i, 'course_name'], response))



if __name__ == "__main__":
    
    students_df = pd.read_csv('tests/mock_data/mock_students_data.csv')
    create_mock_students(students_df)

    courses_df = pd.read_csv('tests/mock_data/mock_courses_data.csv')
    create_mock_courses(courses_df)