from uuid import uuid4
import config
import redis
import scapp_pb2 as pb
import scapp_pb2_grpc as rpc

r = redis.Redis(host='localhost', port=6379)


def generate_course_id():
    return uuid4().hex


def store_course(course):
    all_courses = pb.AllCourses()
    if not r.get("all_courses"):
        print('No course data in redis, creating...')
        all_courses.courses.append(course)
    else:
        all_courses_string = r.get("all_courses")
        all_courses.ParseFromString(all_courses_string)
        all_courses.courses.append(course)

    for course in all_courses.courses:
        print(course)
    all_courses_string = all_courses.SerializeToString()
    r.set("all_courses", all_courses_string)


def get_course_by_id(name):
    all_courses = pb.AllCourses()
    if not r.get("all_students"):
        print('No student data in redis, creating...')
    else:
        all_students_string = r.get("all_students")
        all_students.ParseFromString(all_students_string)
    
    for student in all_students.students:
        if student.student_id == id:
            return student
