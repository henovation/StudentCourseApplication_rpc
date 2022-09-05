import unittest
import random
import client
import helper.student_service_helper as shelper
import helper.course_service_helper as chelper
from helper.utils import get_studentList, get_courseList


class StudentTest(unittest.TestCase):
    
    def setUp(self) -> None:
        return super().setUp()

    def test_createStudent(self):
        try:
            self.assertTrue(client.create_student(name="TestStudentName", email="test@gmail.com"), "True")
        except:
            self.assertRaisesRegex(ValueError, 'Student name has been registered, ignore~')

    def test_updateStudent(self):
        st_lst = get_studentList()
        last_id = list(st_lst.values())[-1]
        "update name to an exist student id"
        self.assertTrue(client.update_student(sid=last_id, name="I'm an updated test name"))


    def test_getStudentGradePointAverage(self):
        try:
            st_lst = get_studentList()
            sid = random.choice(list(st_lst.values()))
            gpa = shelper.calculate_gpa(sid)
            self.assertGreaterEqual(gpa, 0)
            self.assertLessEqual(gpa, 4)
        except:
            self.assertRaisesRegex(ValueError, "Grade not found for student: .*")

class CourseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.st_lst = get_studentList()
        self.sid = random.choice(list(self.st_lst.values()))
        self.cr_lst = get_courseList()
        course_name = random.choice(list(self.cr_lst.keys()))
        self.cid = self.cr_lst.get(course_name)
        return super().setUp()

    def test_createCourse(self):
        try:
            self.assertTrue(client.create_course(course_name="GRPC_HANDS_ON", credits=3, start_date="2022/08/15", end_date="2022/09/08", course_schedule="6PM Every Thur & Mon"))
        except:
            self.assertRaisesRegex(ValueError, "Course name conflict with existing courses, please rename the new course!")


    def test_updateCourse(self):
        try:
            cr_lst = get_courseList()
            cid = cr_lst.get("GRPC_HANDS_ON")
            self.assertTrue(client.update_course(cid=cid, course_name="GRPC_hands_on_project", credits=3, start_date="2022/08/15", end_date="2022/09/08", course_schedule="6PM Every Thur & Mon"))
        except:
            self.assertRaisesRegex(ValueError, "Course has been updated, ignore~")


    def test_addStudentToCourse(self):
        """ Add student test """
        try:
            for i in range(len(list(self.st_lst))):
                sid = list(self.st_lst.values())[i]
                self.assertTrue(chelper.add_student_to_course(sid=sid, cid=self.cid))
        except:
            self.assertRaisesRegex(ValueError, ".* has been registered! Skipping registering...")

    def test_removeStudentToCourse(self):
        """ Add then remove the same student id with same course id """
        try:
            self.assertTrue(chelper.add_student_to_course(sid=self.sid, cid=self.cid))
        except:
            self.assertRaisesRegex(ValueError, ".* has been registered! Skipping registering...")
        try:
            self.assertTrue(chelper.remove_student_from_course(sid=self.sid, cid=self.cid))
        except:
            self.assertRaisesRegex(ValueError, ".* not found in *! Skip removing ...")


    def test_setStudentGradeForCourse(self):
        """ Test setting all students' grade all to the specified course """
        try:
            grades = ["A", "B", "C", "D", "E"]
            registered_students = chelper.get_registered_students(self.cid)
            for sid in registered_students:
                self.assertTrue(chelper.set_student_grade_to_course(sid=sid, cid=self.cid, grade=random.choice(grades)))
        except:
            self.assertRaisesRegex(ValueError, '.* has been graded! Skip grading ...')


    def test_calculateCourseAverage(self):
        """  between 0-4, if the random chosen course's registered student number less than 5, then run test_setStudentGradeForCourse first """
        try:
            ave = chelper.calculate_ave(self.cid)
            self.assertGreaterEqual(ave, 0)
            self.assertLessEqual(ave, 4)
        except:
            self.assertRaisesRegex(ValueError, 'Some students may not been graded yet!')
        
            
    def test_getStudentGrade(self):
        grades = ["A", "B", "C", "D", "E"]
        try:
            self.assertIn(chelper.get_student_grade_from_course(self.sid, self.cid), grades)
        except:
            self.assertRaisesRegex(ValueError, 'Grade not found for student: .*')


if __name__ == '__main__':
    unittest.main()