import grpc
from google.protobuf.json_format import MessageToJson
import grpc_app.helper.generated.scapp_pb2 as pb
import grpc_app.helper.generated.scapp_pb2_grpc as rpc
import grpc_app.helper.SCArgParser as SCArgParser
import grpc_app.helper.student_service_helper as shelper
import grpc_app.helper.course_service_helper as chelper
from grpc_app.helper.utils import *

def create_student(name=None, email=None):
    if not name:
        name = input("Enter student name: ")
    if not email:
        email = input("Enter student email: ")
    with grpc.insecure_channel('localhost:1024') as channel:
        stub = rpc.StudentServicesStub(channel)
        response = stub.CreateStudent(pb.CreateStudentRequest(student_name=name, email=email))
        if response.success is False:
            raise ValueError("Creating student fails!")
    print("Successfully created student profile:\nName: {}\nEmail: {}".format(name, email))

def update_student(**kwargs):
    sid = kwargs["sid"]
    with grpc.insecure_channel('localhost:1024') as channel:
        stub = rpc.StudentServicesStub(channel)
        if "name" not in kwargs:
            response = stub.UpdateStudent(pb.UpdateStudentRequest(student_id=sid, email=kwargs['email']))
            print("Successfully updated student profile to:\nID: {}\nEmail: {}".format(sid, kwargs["email"]))
        if "email" not in kwargs:
            response = stub.UpdateStudent(pb.UpdateStudentRequest(student_id=sid, student_name=kwargs['name']))
            print("Successfully updated student profile to:\nID: {}\nName: {}\n".format(sid, kwargs["name"]))
        if "name" in kwargs and "email" in kwargs:
            response = stub.UpdateStudent(pb.UpdateStudentRequest(student_id=sid, student_name=kwargs['name'], email=kwargs['email']))
            print("Successfully updated student profile to:\nID: {}\nName: {}\nEmail: {}".format(sid, kwargs["name"], kwargs["email"]))
        if response.success is False:
            raise ValueError("Update student fails!")


def create_course(**kwargs):
    with grpc.insecure_channel('localhost:1024') as channel:
        stub = rpc.CourseServicesStub(channel)
        response = stub.CreateCourse(pb.CreateCourseRequest(course_name=kwargs["course_name"],credits=kwargs["credits"], start_date=kwargs["start_date"], end_date=kwargs["end_date"], course_schedule=kwargs["course_schedule"]))
        print("Successfully created course profile!")
        if response.success is False:
            raise ValueError("Create course fails!")


def update_course(**kwargs):
    with grpc.insecure_channel('localhost:1024') as channel:
        stub = rpc.CourseServicesStub(channel)
        response = stub.UpdateCourse(pb.UpdateCourseRequest(course_id=kwargs["cid"], course_name=kwargs["course_name"],credits=kwargs["credits"], start_date=kwargs["start_date"], end_date=kwargs["end_date"], course_schedule=kwargs["course_schedule"]))
        print("Successfully updated course profile: {}".format(kwargs))
        if response.success is False:
            raise ValueError("Update course fails!")


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
        get_course_data_by_id(args.cid, kv)

    if args.create_student_by_input:
        create_student()

    if args.createStudent:
        if args.name and args.email:
            create_student(args.name, args.email)
        else:
            print('Please make sure both name and email provided!')

    if args.updateStudent:
        if not args.sid:
            print("Student ID required!!")
            return
        kv = dict()
        kv["sid"] = args.sid
        if args.name:
            kv["name"] = args.name
        if args.email:
            kv["email"] = args.email
        update_student(**kv)

    if args.getCoursesOfStudent:
        get_student_course(args.sid)

    if args.getStudentGradePointAverage:
        response = shelper.calculate_gpa(args.sid)
        print(response)

    if args.createCourse:
        try:
            kv = dict()
            kv["course_name"] = args.course_name
            if not args.credits:
                kv["credits"] = 3
            else:
                kv["credits"] = args.credits
            kv["start_date"] = args.start_date
            kv["end_date"] = args.end_date
            kv["course_schedule"] = args.end_date
            create_course(**kv)
        except:
            print("Make sure all required inputs provided!")


    if args.updateCourse:
        if not args.cid:
            print("Course ID required!!")
            return
        kv = dict()
        kv["cid"] = args.cid
        if args.course_name:
            kv["course_name"] = args.course_name
        if not args.credits:
            kv["credits"] = 3
        else:
            kv["credits"] = args.credits
        if args.credits:
            kv["credits"] = args.credits
        if args.start_date:
            kv["start_date"] = args.start_date
        if args.end_date:
            kv["end_date"] = args.end_date
        if args.end_date:
            kv["course_schedule"] = args.end_date
        update_course(**kv)


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