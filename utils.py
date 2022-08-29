from datetime import datetime
import redis
from uuid import uuid4
import config
from google.protobuf.timestamp_pb2 import Timestamp
import scapp_pb2 as pb
import scapp_pb2_grpc as rpc

db = redis.Redis(host='localhost', port=6379)

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
def get_student_id():
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
            return student


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
            # print(course)
            return course


