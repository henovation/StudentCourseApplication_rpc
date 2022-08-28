import scapp_pb2 as pb
import scapp_pb2_grpc as rpc
import sys
import grpc
import redis

r = redis.Redis(host='localhost', port=6379)


def create_student():
    name = input("Enter student name: ")
    email = input("Enter student email: ")
    with grpc.insecure_channel('localhost:1024') as channel:
        stub = rpc.StudentServicesStub(channel)
        response = stub.CreateStudent(pb.CreateStudentRequest(student_name=name, email=email))
        if response.success:
            print("Successfully created your profile: \n", name, email)

def list_student():
    if not r.get("all_students"):
        print('No student data in redis')
    else:
        all_students = pb.AllStudents()
        all_students_string = r.get("all_students")
        all_students.ParseFromString(all_students_string)

    for student in all_students.students:
        print(student)

def list_course():
    if not r.get("all_courses"):
        print('No course data in redis')
    else:
        all_courses = pb.AllCourses()
        all_courses_string = r.get("all_courses")
        all_courses.ParseFromString(all_courses_string)

    for course in all_courses.courses:
        print(course)

if __name__ == "__main__":

    # create_student()
    # list_student()
    list_course()