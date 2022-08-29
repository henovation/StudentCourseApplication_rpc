from concurrent.futures import ThreadPoolExecutor
from google.protobuf.json_format import MessageToJson
from google.protobuf.timestamp_pb2 import Timestamp

import grpc
import helper.generated.scapp_pb2 as pb
import helper.generated.scapp_pb2_grpc as rpc
import helper.student_service_helper as shelper
import helper.course_service_helper as chelper
import helper.utils as utils


class StudentServices(rpc.StudentServicesServicer):
    def CreateStudent(self, request, context):
        """ Create a student info """
        try:
            create_time = Timestamp()
            create_time.GetCurrentTime()
            new_student = pb.Student(
                student_id=utils.create_student_id(),
                student_name=request.student_name,
                email=request.email,
                credit_capacity=36,
                create_student_timestamp=create_time,
                last_modified_timestamp=create_time,
            )
            shelper.store_student(new_student)
            success = True
        except:
            print('Error when creating a student with input data:\n{}'.format(request))
            success = False
        return pb.CreateStudentResponse(success=success)

    def UpdateStudent(self, request, context):
        """ Update a student info """
        shelper.update_student(request)
        success = True
        return pb.UpdateStudentResponse(success=success)

    def GetCourse(self, request, context):
        """ Get Courses list of a specified student """
        if utils.validate_student_id(request.student_id):
            student = utils.get_student_by_id(request.student_id)
            registered_courses_ids = student.registered_courses
            course_list = pb.AllCourses()
            for course_id in registered_courses_ids:
                course_list.courses.append(utils.get_course_data_by_id(course_id))
            # print(MessageToJson(course_list))
            return pb.GetCoursesResponse(course_list=course_list.courses)
        else:
            raise ValueError("Not valid student_id: {}".format(request.student_id))

    def GetStudentGPA(self, request, context):
        """ Calculate a specified student's GPA """
        if utils.validate_student_id(request.student_id):
            gpa = shelper.calculate_gpa(request.student_id)
            return pb.GetStudentGPAResponse(gpa=gpa)
        else:
            raise ValueError("Not valid student_id: {}".format(request.student_id))


class CourseServcies(rpc.CourseServicesServicer):
    def CreateCourse(self, request, context):
        """ Create a course info """
        # try:
        create_time = Timestamp()
        create_time.GetCurrentTime()
        new_course = pb.Course(
            course_id=utils.generate_course_id(),
            course_name=request.course_name,
            credits=request.credits,
            start_date=request.start_date,
            end_date=request.end_date,
            start_date_timestamp=utils.get_proto_timestamp_from_string(request.start_date),
            end_date_timestamp=utils.get_proto_timestamp_from_string(request.end_date),
            course_schedule=request.course_schedule,
            create_course_timestamp=create_time,
            last_modified_timestamp=create_time,
        )
        chelper.store_course(new_course)
        success = True
        # except:
        #     print('Error when creating a course with input data:\n{}'.format(request))
        #     success = False
        return pb.CreateCourseResponse(success=success)

    def UpdateCourse(self, request, context):
        """ Update a course info """
        chelper.update_course(request)
        success = True
        return pb.UpdateStudentResponse(success=success)

    def AddStudent(self, request, context):
        """ Add a student to a course by id """
        try:
            if utils.validate_student_id(request.student_id) and utils.validate_course_id(request.course_id):
                success = chelper.add_student_to_course(request.student_id, request.course_id)
            else:
                print('Not a valid student or course id input:\n{}'.format(request))
                success = False
        except:
            print('Exception Error when adding a student to a course  with input data:\n{}'.format(request))
            success = False
        return pb.AddStudentToCourseResponse(success=success)

    def RemoveStudent(self, request, context):
        """ Remove a student to a course by id """
        try:
            if utils.validate_student_id(request.student_id) and utils.validate_course_id(request.course_id):
                success = chelper.remove_student_from_course(request.student_id, request.course_id)
            else:
                print('Not a valid student or course id input:\n{}'.format(request))
                success = False
        except:
            print('Exception Error when removing a student from a course with input data:\n{}'.format(request))
            success = False
        return pb.RemoveStudentFromCourseResponse(success=success)

    def CalculateAve(self, request, context):
        """ Calculate the average of a specified course """
        average = chelper.calculate_ave(request.course_id)
        return pb.CalculateCourseAverageResponse(average=average)


    def GetStudent(self, request, context):
        """ Return a list of students registered in a specified course """   
        if utils.validate_course_id(request.course_id):
            registered_student_ids = chelper.get_registered_students(request.course_id)
            student_list = pb.AllStudents()
            for sid in registered_student_ids:
                student_list.students.append(utils.get_student_by_id(sid))
            print(MessageToJson(student_list))
            return pb.GetStudentsResponse(student_list=student_list.students)
        else:
            raise ValueError("Not valid course_id: {}".format(request.course_id))

    def SetStudentGrade(self, request, context):
        """ Set grade to a specified student registered in a specified course """   
        if utils.validate_student_id(request.student_id) and utils.validate_course_id(request.course_id) and utils.validate_grade(request.grade.upper()):
            success = chelper.set_student_grade_to_course(request.student_id, request.course_id, request.grade)
        else:
            print('Not a valid input:\n{}'.format(request))
            success = False
        return pb.SetStudentGradeResponse(success=success)

    def GetStudentGrade(self, request, context):
        """ Get grade to a specified student registered in a specified course """
        if utils.validate_student_id(request.student_id) and utils.validate_course_id(request.course_id):
            grade = chelper.get_student_grade_from_course(request.student_id, request.course_id)
        else:
            raise ValueError('Not a valid student or course id input:\n{}'.format(request))
        return pb.GetStudentGradeResponse(grade=grade)

    def ResetCourseData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


if __name__ == '__main__':
    import config

    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    rpc.add_StudentServicesServicer_to_server(StudentServices(), server)
    rpc.add_CourseServicesServicer_to_server(CourseServcies(), server)

    addr = f'[::]:{config.port}'
    server.add_insecure_port(addr)
    server.start()

    print('server ready on %s', addr)
    server.wait_for_termination()