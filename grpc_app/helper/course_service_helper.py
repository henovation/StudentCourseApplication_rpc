import helper.generated.scapp_pb2 as pb
from helper.utils import db
import helper.utils as utils

def store_course(new_course):
    all_courses = pb.AllCourses()
    if not db.get("all_courses"):
        print('No course data in redis, creating...')
        all_courses.courses.append(new_course)
    else:
        all_courses_string = db.get("all_courses")
        all_courses.ParseFromString(all_courses_string)
        for course in all_courses.courses:
            if course.course_name == new_course.course_name:
                raise ValueError("Course name conflict with existing courses, please rename the new course!")
        all_courses.courses.append(new_course)

    all_courses_string = all_courses.SerializeToString()
    db.set("all_courses", all_courses_string)


def update_course(updated_course):
    all_courses = pb.AllCourses()
    all_courses_string = db.get("all_courses")
    all_courses.ParseFromString(all_courses_string)

    for course in all_courses.courses:
        if course.course_id == updated_course.course_id:
            if updated_course.course_name:
                if course.course_name == updated_course.course_name:
                    raise ValueError("Course has been updated, ignore~")
                course.course_name = updated_course.course_name
            if updated_course.credits:
                course.credits = updated_course.credits
            if updated_course.start_date:
                course.start_date = updated_course.start_date
                dt = utils.convert_to_datetime_from_string(updated_course.start_date)
                course.end_date_timestamp.FromDatetime(dt)
            if updated_course.end_date:
                course.end_date = updated_course.end_date
                dt = utils.convert_to_datetime_from_string(updated_course.end_date)
                course.end_date_timestamp.FromDatetime(dt)
            if updated_course.course_schedule:
                course.course_schedule = updated_course.course_schedule
            course.last_modified_timestamp.GetCurrentTime()
            break
    
    all_courses_string = all_courses.SerializeToString()
    db.set("all_courses", all_courses_string)



def add_student_to_course(sid: int, cid: str):
    all_courses = pb.AllCourses()
    all_courses_string = db.get("all_courses")
    all_courses.ParseFromString(all_courses_string)
    all_students = pb.AllStudents()
    all_students_string = db.get("all_students")
    all_students.ParseFromString(all_students_string)
    
    for course in all_courses.courses:
        if course.course_id == cid:
            if sid not in course.enrolled_students:
                course.enrolled_students.append(sid)
                print('Added student_id {} to course_id {}'.format(sid, cid))
            else:
                print('Student_id: {} has been registered! Skipping registering...'.format(sid))
                return False
            course.last_modified_timestamp.GetCurrentTime()
            break
    
    for student in all_students.students:
        if student.student_id == sid:
            student.registered_courses.append(cid)
            student.last_modified_timestamp.GetCurrentTime()
            break
            
    all_courses_string = all_courses.SerializeToString()
    db.set("all_courses", all_courses_string)
    all_students_string = all_students.SerializeToString()
    db.set("all_students", all_students_string)
    return True


def remove_student_from_course(sid: int, cid: str):
    all_courses = pb.AllCourses()
    all_courses_string = db.get("all_courses")
    all_courses.ParseFromString(all_courses_string)
    all_students = pb.AllStudents()
    all_students_string = db.get("all_students")
    all_students.ParseFromString(all_students_string)
    
    for course in all_courses.courses:
        if course.course_id == cid:
            if sid in course.enrolled_students:
                for i, gmap in enumerate(course.grades):
                    if sid in gmap.grade:
                        course.grades.pop(i)
                        print('Removed student\'s grade {} '.format(gmap.grade[sid]))
                course.enrolled_students.remove(sid)
                print('Removed student {} from course_id {}'.format(sid, cid))
            else:
                print('Student_id: {} not found in {}! Skip removing ...'.format(sid, cid))
                return False
            course.last_modified_timestamp.GetCurrentTime()
            all_courses_string = all_courses.SerializeToString()
            db.set("all_courses", all_courses_string)
            break
    
    # remove course_id from student's registered_courses
    for student in all_students.students:
        if student.student_id == sid:
            student.registered_courses.remove(cid)
            student.last_modified_timestamp.GetCurrentTime()
            all_students_string = all_students.SerializeToString()
            db.set("all_students", all_students_string)
            break
    return True
            

def get_registered_students(cid: str):
    all_courses = pb.AllCourses()
    all_courses_string = db.get("all_courses")
    all_courses.ParseFromString(all_courses_string)
    for course in all_courses.courses:
        if course.course_id == cid:
            registered_students = course.enrolled_students
            return registered_students


def set_student_grade_to_course(sid: int, cid: str, grade: str):
    all_courses = pb.AllCourses()
    all_courses_string = db.get("all_courses")
    all_courses.ParseFromString(all_courses_string)
    
    for course in all_courses.courses:
        if course.course_id == cid:

            if sid in course.enrolled_students:
                """ validate if student has been graded """
                for gmap in course.grades:
                    if sid in gmap.grade:
                        print('student: {} has been graded! Skip grading ...'.format(sid))
                        return False
                
                student_grade = pb.Grade()
                student_grade.grade[sid] = grade.upper()
                course.grades.append(student_grade)
                print('Successfully set grade {} to student {}'.format(student_grade, sid))
            else:
                print('Student_id: {} not found in class!'.format(sid))
                return False
            course.last_modified_timestamp.GetCurrentTime()
            all_courses_string = all_courses.SerializeToString()
            db.set("all_courses", all_courses_string)
            break
    return True
            

def get_student_grade_from_course(sid: int, cid: str):
    all_courses = pb.AllCourses()
    all_courses_string = db.get("all_courses")
    all_courses.ParseFromString(all_courses_string)
    
    for course in all_courses.courses:
        if course.course_id == cid:
            if sid in course.enrolled_students:
                for gmap in course.grades:
                    if sid in gmap.grade:
                        return gmap.grade[sid]
    raise ValueError('Grade not found for student: {} with course {}'.format(sid, cid))


def calculate_ave(cid: str):
    all_courses = pb.AllCourses()
    all_courses_string = db.get("all_courses")
    all_courses.ParseFromString(all_courses_string)
    
    grades = ["A", "B", "C", "D", "E"]
    scores = [5, 4, 3, 2, 1]
    grades_dict = dict(zip(grades, scores))

    for course in all_courses.courses:
        if course.course_id == cid:
            registered_students = course.enrolled_students
            number_of_registered_students = len(registered_students)
            total_score = 0
            if len(registered_students) == len(course.grades) and len(registered_students) != 0:
                for gmap in course.grades:
                    idx = len(registered_students)
                    for i in range(idx):
                        if gmap.grade[registered_students[i]]:
                            matched_student_id = registered_students[i]
                            registered_students.remove(matched_student_id)
                            # print(registered_students)
                            break
                    total_score += grades_dict.get(gmap.grade[matched_student_id])
                return total_score/number_of_registered_students
            else:
                raise ValueError('Some students may not been graded yet!')
    raise ValueError('Course: {} not found in database!'.format(cid))


def get_course_credit(cid: str):
    all_courses = pb.AllCourses()
    all_courses_string = db.get("all_courses")
    all_courses.ParseFromString(all_courses_string)
    for course in all_courses.courses:
        if course.course_id == cid:
            return course.credits
    raise ValueError('Course: {} not found in database!'.format(cid))
