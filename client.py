from traceback import print_stack
import grpc
from google.protobuf.json_format import MessageToJson
import helper.generated.scapp_pb2 as pb
import helper.generated.scapp_pb2_grpc as rpc
import helper.SCArgParser as SCArgParser
import helper.student_service_helper as shelper
import helper.course_service_helper as chelper
from helper.utils import db


def cmd_create_student(name=None, email=None):
    if not name:
        name = input("Enter student name: ")
    if not email:
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


def main(args=None):
    if not args:
        args = SCArgParser.ArgParser().parse()

    if args.CreateStudent:
        if args.name and args.email:
            cmd_create_student(args.name, args.email)
        else:
            cmd_create_student()
        return

    if args.UpdateStudent:
        if not args.sid:
            print('Student id is required', '\033[95m')
            return
        if not args.name:
            print('No student id specified', '\033[94m')
            return
        sid = int(args.sid)
        chelper.add_student_to_course(sid, args.cid)
        return

    if args.GetStudentCourse:
        if not args.cid:
            print('No course id specified', '\033[95m')
            return
        elif not args.sid:
            print('No student id specified', '\033[94m')
            return
        sid = int(args.sid)
        chelper.add_student_to_course(sid, args.cid)
        return

    if args.GetStudentGPA:
        if not args.cid:
            print('No course id specified', '\033[95m')
            return
        elif not args.sid:
            print('No student id specified', '\033[94m')
            return
        sid = int(args.sid)
        chelper.add_student_to_course(sid, args.cid)
        return

    if args.CreateCourse:
        if not args.cid:
            print('No course id specified', '\033[95m')
            return
        elif not args.sid:
            print('No student id specified', '\033[94m')
            return
        sid = int(args.sid)
        chelper.add_student_to_course(sid, args.cid)
        return

    if args.UpdateCourse:
        if not args.cid:
            print('No course id specified', '\033[95m')
            return
        elif not args.sid:
            print('No student id specified', '\033[94m')
            return
        sid = int(args.sid)
        chelper.add_student_to_course(sid, args.cid)
        return

    if args.AddStudent:
        if not args.cid:
            print('No course id specified', '\033[95m')
            return
        elif not args.sid:
            print('No student id specified', '\033[94m')
            return
        sid = int(args.sid)
        chelper.add_student_to_course(sid, args.cid)
        return

    if args.RemoveStudent:
        if not args.cid:
            print('No course id specified', '\033[95m')
            return
        elif not args.sid:
            print('No student id specified', '\033[94m')
            return
        sid = int(args.sid)
        chelper.add_student_to_course(sid, args.cid)
        return

    if args.CalculateAve:
        if not args.cid:
            print('No course id specified', '\033[95m')
            return
        elif not args.sid:
            print('No student id specified', '\033[94m')
            return
        sid = int(args.sid)
        chelper.add_student_to_course(sid, args.cid)
        return

    if args.GetStudent:
        if not args.cid:
            print('No course id specified', '\033[95m')
            return
        elif not args.sid:
            print('No student id specified', '\033[94m')
            return
        sid = int(args.sid)
        chelper.add_student_to_course(sid, args.cid)
        return

    if args.SetStudentGrade:
        if not args.cid:
            print('No course id specified', '\033[95m')
            return
        elif not args.sid:
            print('No student id specified', '\033[94m')
            return
        sid = int(args.sid)
        chelper.add_student_to_course(sid, args.cid)
        return

    if args.GetStudentGrade:
        if not args.cid:
            print('No course id specified', '\033[95m')
            return
        elif not args.sid:
            print('No student id specified', '\033[94m')
            return
        sid = int(args.sid)
        chelper.add_student_to_course(sid, args.cid)
        return

    if args.ResetData:
        if not args.cid:
            print('No course id specified', '\033[95m')
            return
        elif not args.sid:
            print('No student id specified', '\033[94m')
            return
        sid = int(args.sid)
        chelper.add_student_to_course(sid, args.cid)
        return


    # list_student()
    # list_course()

    # utils.get_student_by_id(30001)
    # utils.get_course_data_by_id("55e39268300f46c0a39fa34572c7d097")


if __name__ == "__main__":
    main()