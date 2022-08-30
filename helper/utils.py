import redis
from uuid import uuid4
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf.json_format import MessageToJson
import config
import helper.generated.scapp_pb2 as pb

db = redis.Redis(host='localhost', port=6379)

# <---- Datetime processing related utils from here ---->
def convert_to_datetime_from_string(dt_string: str):
    ymd = dt_string.split('-')
    dt = datetime(int(ymd[0]), int(ymd[1]), int(ymd[2]))
    return dt

def get_proto_timestamp_from_string(dt_string: str):
    timestamp = Timestamp()
    dt = convert_to_datetime_from_string(dt_string)
    timestamp.FromDatetime(dt)
    return timestamp


# <---- Validation related utils from here ---->
def validate_student_id(sid: int):
    all_students = pb.AllStudents()
    if not db.get("all_students"):
        print('No student data in redis!')
    else:
        all_students_string = db.get("all_students")
        all_students.ParseFromString(all_students_string)
    
    for student in all_students.students:
        if student.student_id == sid:
            return True
    raise ValueError("Student_id: {} not valid!".format(sid))
    

def validate_course_id(id: str):
    all_courses = pb.AllCourses()
    if not db.get("all_courses"):
        print('No course data in redis, creating...')
    else:
        all_courses_string = db.get("all_courses")
        all_courses.ParseFromString(all_courses_string)
    
    for course in all_courses.courses:
        if course.course_id == id:
            # print('course_id: {} valid!'.format(id))
            return True
    return False

def validate_grade(grade: str):
    grades = ["A", "B", "C", "D", "E"]
    if grade in grades:
        return True
    else:
        raise ValueError('Wrong grade: {} assigned'.format(grade))


# <---- Students related utils from here ---->
def create_student_id():
    if not db.get("all_students"):
        id = config.init_student_id
        print("Initializing student_id: ", id)
    else:
        all_students = pb.AllStudents()
        all_students_string = db.get("all_students")
        all_students.ParseFromString(all_students_string)
        last_id = all_students.students[-1].student_id
        print("Last used ID is: ", last_id)
        id = last_id + 1
    return id


def get_student_by_id(id):
    all_students = pb.AllStudents()
    if not db.get("all_students"):
        print('No student data in redis, creating...')
    else:
        all_students_string = db.get("all_students")
        all_students.ParseFromString(all_students_string)
    
    for student in all_students.students:
        if student.student_id == id:
            print(student)
            return student


def list_all_students():
    if not db.get("all_students"):
        print('No student data in redis')
    else:
        all_students = pb.AllStudents()
        all_students_string = db.get("all_students")
        all_students.ParseFromString(all_students_string)
    [print(MessageToJson(student),'\n\n\n') for student in all_students.students]
        

def get_studentList():
    if not db.get("all_students"):
        print('No student data in redis')
    else:
        all_students = pb.AllStudents()
        all_students_string = db.get("all_students")
        all_students.ParseFromString(all_students_string)

        student_dict = dict()
        for student in all_students.students:
            print('Student Name: {}'.format(student.student_name))
            print('Student_id: {}\n'.format(student.student_id))
            student_dict[student.student_name] = student.student_id
        return student_dict

# <---- Courses related utils from here ---->
def generate_course_id():
    return uuid4().hex


def get_course_data_by_id(cid: str):
    all_courses = pb.AllCourses()
    if not db.get("all_courses"):
        print('No course data in redis.')
    else:
        all_courses_string = db.get("all_courses")
        all_courses.ParseFromString(all_courses_string)
    
    for course in all_courses.courses:
        if course.course_id == cid:
            print(course)
            return course


def list_all_courses():
    if not db.get("all_courses"):
        print('No course data in redis')
    else:
        all_courses = pb.AllCourses()
        all_courses_string = db.get("all_courses")
        all_courses.ParseFromString(all_courses_string)
    [print(MessageToJson(course),'\n\n\n') for course in all_courses.courses]


def get_courseList():
    if not db.get("all_courses"):
        print('No course data in redis')
    else:
        all_courses = pb.AllCourses()
        all_courses_string = db.get("all_courses")
        all_courses.ParseFromString(all_courses_string)

        courses_dict = dict()
        for course in all_courses.courses:
            print('Course Name: {}'.format(course.course_name))
            print('Course_id: {}\n'.format(course.course_id))
            courses_dict[course.course_name] = course.course_id
        # print(courses_dict)
        return courses_dict
