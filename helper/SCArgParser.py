from builtins import object
import argparse

class ArgParser(object):
    def __init__(self):
        def add_arg(*args, **kwargs):
            self.argparser.add_argument(*args, **kwargs)
        
        self.argparser = argparse.ArgumentParser(description="SCA service options")
  
        add_arg('--cid', '-c', help='Course id')
        add_arg('--sid', '-s', type=int, help='Student id')
        add_arg('--grade', '-g', type=str, help='Grade. ["A","B","C","D","E"]')
        add_arg('--name', '-n', help='Assign student name')
        add_arg('--email', '-e', help='Assign student email')
        add_arg('--course_name', help='Assign course name')
        add_arg('--credits', help='Assign course credits')
        add_arg('--start_date', type=str, help='Course start date. Currently support format:YYYY-MM-DD')
        add_arg('--end_date', type=str, help='Course end date. Currently support format:YYYY-MM-DD')
        add_arg('--course_schedule', type=str, help='Course schedule info')
        add_arg('--timestamp', '-t', help='Timestamp for reset datebase')

        add_arg('--list_all_students', help='List all students profile', action='store_true')
        add_arg('--get_studentList', help='Get all students\' ID and name only list', action='store_true')
        add_arg('--list_all_courses', help='List all courses\' content', action='store_true')
        add_arg('--get_courseList', help='Get all courses\' ID and name only list', action='store_true')
        add_arg('--get_student_by_id', help='Get student profile by id', action='store_true')
        add_arg('--get_course_by_id', help='Get course content by id', action='store_true')
        add_arg('--create_student_by_input', help='Create a student info without argument. Name and email input required.', action="store_true")

        add_arg('--createStudent', help='Create a student info with argument', action="store_true")
        add_arg('--updateStudent', help='Update a student info', action="store_true")
        add_arg('--getCoursesOfStudent', help='Get Courses list of a specified student', action="store_true")
        add_arg('--getStudentGradePointAverage', help='Calculate a specified student\'s GPA', action="store_true")
        add_arg('--createCourse', help='Create a course info', action="store_true")
        add_arg('--updateCourse', help='Update a course info', action="store_true")
        add_arg('--addStudentToCourse', help='Add a student to a course by id', action="store_true")
        add_arg('--removeStudentFromCourse', help='Remove a student from a course by id', action="store_true")
        add_arg('--calculateCourseAverage', help='Calculate the average of a specified course', action="store_true")
        add_arg('--getStudentsOfCourse', help='Return a list of students\'s id registered in a specified course', action="store_true")
        add_arg('--setStudentGradeForCourse', help='Set grade to a specified student registered in a specified course', action="store_true")
        add_arg('--getStudentGrade', help='Get grade to a specified student registered in a specified course', action="store_true")
        add_arg('--resetDataStore', help='Reset data to the latest status up to the specified timestamp', action="store_true")
        

    def parse(self, args=None):
        if args:
            return self.argparser.parse_args(args)
        return self.argparser.parse_args()