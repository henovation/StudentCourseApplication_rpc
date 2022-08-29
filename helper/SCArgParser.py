from builtins import object
import argparse

class ArgParser(object):
    def __init__(self):
        def add_arg(*args, **kwargs):
            self.argparser.add_argument(*args, **kwargs)
        
        self.argparser = argparse.ArgumentParser(description="SCA service options")
        add_arg('--cid', '-c', help='Course id')
        add_arg('--sid', '-s', help='Student id')
        add_arg('--grade', '-g', help='Grade. ["A","B","C","D","E"]')
        add_arg('--start_date', help='Course start date. Currently support format:YYYY-MM-DD')
        add_arg('--ed_date', help='Course end date. Currently support format:YYYY-MM-DD')
        add_arg('--timestamp', '-t', help='Timestamp for reset datebase')
        add_arg('--name', '-n', help='Assign student name')
        add_arg('--email', '-e', help='Assign student email')
        # add_arg()
        add_arg('--CreateStudent', help='Create a student info.', action='store_true')
        add_arg('--UpdateStudent', help='Update a student info', action='store_true')
        add_arg('--GetStudentCourse', help='Get Courses list of a specified student', action='store_true')
        add_arg('--GetStudentGPA', help='Calculate a specified student\'s GPA', action='store_true')
        add_arg('--CreateCourse', help='Create a course info', action='store_true')
        add_arg('--UpdateCourse', help='Update a course info', action='store_true')
        add_arg('--AddStudent', help='Add a student to a course by id', action='store_true')
        add_arg('--RemoveStudent', help='Remove a student to a course by id', action='store_true')
        add_arg('--CalculateAve', help='Calculate the average of a specified course', action='store_true')
        add_arg('--GetStudent', help='Return a list of students registered in a specified course', action='store_true')
        add_arg('--SetStudentGrade', help='Set grade to a specified student registered in a specified course', action='store_true')
        add_arg('--GetStudentGrade', help='Get grade to a specified student registered in a specified course', action='store_true')
        add_arg('--ResetData', help='Reset data to the latest status up to the specified timestamp', action='store_true')


    def parse(self, args=None):
        if args:
            return self.argparser.parse_args(args)
        return self.argparser.parse_args()