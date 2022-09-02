import unittest
import client
from helper.utils import get_studentList 


class StudentTest(unittest.TestCase):
    
    def setUp(self) -> None:
        return super().setUp()

    # def test_createStudent(self):
    #     self.assertTrue(client.create_student(name="TestStudentName", email="test@gmail.com"), "True")

    # def test_updateStudent(self):
    #     st_lst = get_studentList()
    #     last_id = list(st_lst.values())[-1]
    #     "update name to an exist student id"
    #     self.assertTrue(client.update_student(sid=last_id, name="I'm updated"))

    def test_updateStudent_after(self):
        st_lst = get_studentList()
        last_id = list(st_lst.values())[-1]
        "update name to an non-exist student id"
        self.assertFalse(client.update_student(sid=last_id+1, name="I shouldn't be updated"))

# class CourseTest(unittest.TestCase):
#     def setUp(self) -> None:
#         return super().setUp()



    # def test_updateCourse(self):
    #     self.assertTrue(client.update_student(cid= name="TestName"), "True")

if __name__ == '__main__':
    unittest.main()