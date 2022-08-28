from uuid import uuid4
import config
import redis
import scapp_pb2 as pb
import scapp_pb2_grpc as rpc

r = redis.Redis(host='localhost', port=6379)

def get_student_id():
    if not r.get("all_students"):
        id = config.init_student_id
        print("No student data in redis, use init_student_id: ", id)
    else:
        all_students = pb.AllStudents()
        all_students_string = r.get("all_students")
        all_students.ParseFromString(all_students_string)
        last_id = all_students.students[-1].student_id
        print("Last used ID is: ", last_id)
        id = last_id + 1
    return id


def store_student(student):
    all_students = pb.AllStudents()
    if not r.get("all_students"):
        print('No student data in redis, creating...')
        all_students.students.append(student)
    else:
        all_students_string = r.get("all_students")
        all_students.ParseFromString(all_students_string)
        all_students.students.append(student)

    # for student in all_students.students:
    #     print(student)
    all_students_string = all_students.SerializeToString()
    r.set("all_students", all_students_string)


def get_student_by_id(id):
    all_students = pb.AllStudents()
    if not r.get("all_students"):
        print('No student data in redis, creating...')
    else:
        all_students_string = r.get("all_students")
        all_students.ParseFromString(all_students_string)
    
    for student in all_students.students:
        if student.student_id == id:
            return student
