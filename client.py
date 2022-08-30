from traceback import print_stack
import grpc
from google.protobuf.json_format import MessageToJson
import helper.generated.scapp_pb2 as pb
import helper.generated.scapp_pb2_grpc as rpc
import helper.SCArgParser as SCArgParser
import helper.student_service_helper as shelper
import helper.course_service_helper as chelper
from helper.utils import *
from helper.utils import db


def create_student(name=None, email=None):
    if not name:
        name = input("Enter student name: ")
    if not email:
        email = input("Enter student email: ")
    with grpc.insecure_channel('localhost:1024') as channel:
        stub = rpc.StudentServicesStub(channel)
        response = stub.CreateStudent(pb.CreateStudentRequest(student_name=name, email=email))
        if response.success:
            print("Successfully created your profile: \n", name, email)


def get_student_course(sid: int):
    with grpc.insecure_channel('localhost:1024') as channel:
        stub = rpc.StudentServicesStub(channel)
        registered_courses = stub.GetCourse(pb.GetCourseRequest(student_id=sid))
        [print(MessageToJson(course)) for course in registered_courses.courses]



def main(args=None):
    if not args:
        args = SCArgParser.ArgParser().parse()


    if args.list_all_students:
        list_all_students()

    if args.get_studentList:
        get_studentList()

    if args.list_all_courses:
        list_all_courses()

    if args.get_courseList:
        get_courseList()

    if args.get_student_by_id:
        get_student_by_id(args.sid)

    if args.get_course_by_id:
        get_course_data_by_id(args.cid)



    if args.create_student_by_input:
        create_student()

    if args.createStudent:
        if args.name and args.email:
            create_student(args.name, args.email)
        else:
            print('Please make sure both name and email provided!')

    # if args.updateStudent:

    if args.getCoursesOfStudent:
        get_student_course(args.sid)

    if args.getStudentGradePointAverage:
        response = shelper.calculate_gpa(args.sid)
        print(response)


    # if args.createCourse:

    # if args.updateCourse:


    if args.addStudentToCourse:
        if not args.cid:
            print('No course id specified', '\033[95m')
            return
        elif not args.sid:
            print('No student id specified', '\033[94m')
            return
        chelper.add_student_to_course(args.sid, args.cid)

    if args.removeStudentFromCourse:
        if not args.cid:
            print('No course id specified', '\033[95m')
            return
        elif not args.sid:
            print('No student id specified', '\033[94m')
            return
        chelper.remove_student_from_course(args.sid, args.cid)


    if args.calculateCourseAverage:
        response = chelper.calculate_ave(args.cid)
        print('Average score for course {} is: {}'.format(args.cid, response))

    if args.getStudentsOfCourse:
        response = chelper.get_registered_students(args.cid)
        print(response)


    if args.setStudentGradeForCourse:
        chelper.set_student_grade_to_course(args.sid, args.cid, args.grade)

    if args.getStudentGrade:
        response = chelper.get_student_grade_from_course(args.sid, args.cid)
        print('Student {} got the grade: "{}" for the course {}'.format(args.sid, response, args.cid))

    # if args.resetDataStore:


if __name__ == "__main__":
    main()