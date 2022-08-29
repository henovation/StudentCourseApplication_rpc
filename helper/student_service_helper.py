from helper.course_service_helper import get_student_grade_from_course, get_course_credit
import helper.generated.scapp_pb2 as pb
from helper.utils import db


def store_student(student):
    all_students = pb.AllStudents()
    if not db.get("all_students"):
        print('No student data in redis, creating...')
        all_students.students.append(student)
    else:
        all_students_string = db.get("all_students")
        all_students.ParseFromString(all_students_string)
        all_students.students.append(student)

    all_students_string = all_students.SerializeToString()
    db.set("all_students", all_students_string)


def update_student(updated_student):
    all_students = pb.AllStudents()
    all_students_string = db.get("all_students")
    all_students.ParseFromString(all_students_string)

    for student in all_students.students:
        if student.student_id == updated_student.student_id:
            if updated_student.student_name:
                student.student_name = updated_student.student_name
            if updated_student.email:
                student.email = updated_student.email
            student.last_modified_timestamp.GetCurrentTime()
            break
    all_students_string = all_students.SerializeToString()
    db.set("all_students", all_students_string)

    
def calculate_gpa(sid: int):
    all_students = pb.AllStudents()
    all_students_string = db.get("all_students")
    all_students.ParseFromString(all_students_string)
    grades = ["A", "B", "C", "D", "E"]
    scores = [5, 4, 3, 2, 1]
    grades_dict = dict(zip(grades, scores))

    for student in all_students.students:
        if student.student_id == sid:
            registered_courses_ids = student.registered_courses
            break
    
    print('\nStart calculating student {} GPA:'.format(sid))
    total_scores = 0
    total_credits = 0
    for cid in registered_courses_ids:
        grade = get_student_grade_from_course(sid, cid)
        credit = get_course_credit(cid)
        print('Grade: {} for course: {}'.format(grade, cid))
        total_scores += grades_dict.get(grade) * credit
        total_credits += credit
    return total_scores/total_credits
