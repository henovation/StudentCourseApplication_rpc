import scapp_pb2 as pb
import scapp_pb2_grpc as rpc
import grpc
from google.protobuf.json_format import MessageToJson
from utils import db


def cmd_create_student():
    name = input("Enter student name: ")
    email = input("Enter student email: ")
    with grpc.insecure_channel('localhost:1024') as channel:
        stub = rpc.StudentServicesStub(channel)
        response = stub.CreateStudent(pb.CreateStudentRequest(student_name=name, email=email))
        if response.success:
            print("Successfully created your profile: \n", name, email)


def list_student():
    if not db.get("all_students"):
        print('No student data in redis')
    else:
        all_students = pb.AllStudents()
        all_students_string = db.get("all_students")
        all_students.ParseFromString(all_students_string)
    [print(MessageToJson(student)) for student in all_students.students]
        

def list_course():
    if not db.get("all_courses"):
        print('No course data in redis')
    else:
        all_courses = pb.AllCourses()
        all_courses_string = db.get("all_courses")
        all_courses.ParseFromString(all_courses_string)
    [print(MessageToJson(course)) for course in all_courses.courses]
    # for course in all_courses.courses:
    #     print(course.grades)


if __name__ == "__main__":

    # cmd_create_student()
    # list_student()
    list_course()

    # utils.get_student_by_id(30001)
    # utils.get_course_data_by_id("55e39268300f46c0a39fa34572c7d097")
