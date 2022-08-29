# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scapp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bscapp.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"&\n\nAllCourses\x12\x18\n\x07\x63ourses\x18\x01 \x03(\x0b\x32\x07.Course\"\xb9\x03\n\x06\x43ourse\x12\x11\n\tcourse_id\x18\x01 \x01(\t\x12\x13\n\x0b\x63ourse_name\x18\x02 \x01(\t\x12\x0f\n\x07\x63redits\x18\x03 \x01(\x03\x12\x12\n\nstart_date\x18\x04 \x01(\t\x12\x38\n\x14start_date_timestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08\x65nd_date\x18\x06 \x01(\t\x12\x36\n\x12\x65nd_date_timestamp\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x17\n\x0f\x63ourse_schedule\x18\x08 \x01(\t\x12\x19\n\x11\x65nrolled_students\x18\t \x03(\x03\x12\x18\n\x10\x64ropped_students\x18\n \x03(\x03\x12\x16\n\x06grades\x18\x0b \x03(\x0b\x32\x06.Grade\x12;\n\x17\x63reate_course_timestamp\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12;\n\x17last_modified_timestamp\x18\r \x01(\x0b\x32\x1a.google.protobuf.Timestamp\")\n\x0b\x41llStudents\x12\x1a\n\x08students\x18\x01 \x03(\x0b\x32\x08.Student\"\xf2\x01\n\x07Student\x12\x12\n\nstudent_id\x18\x01 \x01(\x03\x12\x14\n\x0cstudent_name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x17\n\x0f\x63redit_capacity\x18\x04 \x01(\x03\x12\x1a\n\x12registered_courses\x18\x05 \x03(\t\x12<\n\x18\x63reate_student_timestamp\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12;\n\x17last_modified_timestamp\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"W\n\x05Grade\x12 \n\x05grade\x18\x01 \x03(\x0b\x32\x11.Grade.GradeEntry\x1a,\n\nGradeEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\";\n\x14\x43reateStudentRequest\x12\x14\n\x0cstudent_name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\"(\n\x15\x43reateStudentResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"O\n\x14UpdateStudentRequest\x12\x12\n\nstudent_id\x18\x01 \x01(\x03\x12\x14\n\x0cstudent_name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"(\n\x15UpdateStudentResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"z\n\x13\x43reateCourseRequest\x12\x13\n\x0b\x63ourse_name\x18\x01 \x01(\t\x12\x0f\n\x07\x63redits\x18\x02 \x01(\x03\x12\x12\n\nstart_date\x18\x03 \x01(\t\x12\x10\n\x08\x65nd_date\x18\x04 \x01(\t\x12\x17\n\x0f\x63ourse_schedule\x18\x05 \x01(\t\"\'\n\x14\x43reateCourseResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x8d\x01\n\x13UpdateCourseRequest\x12\x11\n\tcourse_id\x18\x01 \x01(\t\x12\x13\n\x0b\x63ourse_name\x18\x02 \x01(\t\x12\x0f\n\x07\x63redits\x18\x03 \x01(\x03\x12\x12\n\nstart_date\x18\x04 \x01(\t\x12\x10\n\x08\x65nd_date\x18\x05 \x01(\t\x12\x17\n\x0f\x63ourse_schedule\x18\x06 \x01(\t\"\'\n\x14UpdateCourseResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"B\n\x19\x41\x64\x64StudentToCourseRequest\x12\x12\n\nstudent_id\x18\x01 \x01(\x03\x12\x11\n\tcourse_id\x18\x02 \x01(\t\"-\n\x1a\x41\x64\x64StudentToCourseResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"G\n\x1eRemoveStudentFromCourseRequest\x12\x12\n\nstudent_id\x18\x01 \x01(\x03\x12\x11\n\tcourse_id\x18\x02 \x01(\t\"2\n\x1fRemoveStudentFromCourseResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"2\n\x1d\x43\x61lculateCourseAverageRequest\x12\x11\n\tcourse_id\x18\x01 \x01(\t\"1\n\x1e\x43\x61lculateCourseAverageResponse\x12\x0f\n\x07\x61verage\x18\x01 \x01(\x01\"&\n\x10GetCourseRequest\x12\x12\n\nstudent_id\x18\x01 \x01(\x03\"2\n\x12GetCoursesResponse\x12\x1c\n\x0b\x63ourse_list\x18\x01 \x03(\x0b\x32\x07.Course\"\'\n\x12GetStudentsRequest\x12\x11\n\tcourse_id\x18\x01 \x01(\t\"5\n\x13GetStudentsResponse\x12\x1e\n\x0cstudent_list\x18\x01 \x03(\x0b\x32\x08.Student\"*\n\x14GetStudentGPARequest\x12\x12\n\nstudent_id\x18\x01 \x01(\x03\"$\n\x15GetStudentGPAResponse\x12\x0b\n\x03gpa\x18\x01 \x01(\x01\"N\n\x16SetStudentGradeRequest\x12\x12\n\nstudent_id\x18\x01 \x01(\x03\x12\x11\n\tcourse_id\x18\x02 \x01(\t\x12\r\n\x05grade\x18\x03 \x01(\t\"*\n\x17SetStudentGradeResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"?\n\x16GetStudentGradeRequest\x12\x12\n\nstudent_id\x18\x01 \x01(\x03\x12\x11\n\tcourse_id\x18\x02 \x01(\t\"(\n\x17GetStudentGradeResponse\x12\r\n\x05grade\x18\x01 \x01(\t\"H\n\x17ResetStudentDataRequest\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"G\n\x16ResetCourseDataRequest\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"_\n\x16ResetDataStoreResponse\x12\"\n\x1areset_student_data_success\x18\x01 \x01(\x08\x12!\n\x19reset_course_data_success\x18\x02 \x01(\x08\x32\xcd\x02\n\x0fStudentServices\x12>\n\rCreateStudent\x12\x15.CreateStudentRequest\x1a\x16.CreateStudentResponse\x12>\n\rUpdateStudent\x12\x15.UpdateStudentRequest\x1a\x16.UpdateStudentResponse\x12\x33\n\tGetCourse\x12\x11.GetCourseRequest\x1a\x13.GetCoursesResponse\x12>\n\rGetStudentGPA\x12\x15.GetStudentGPARequest\x1a\x16.GetStudentGPAResponse\x12\x45\n\x10ResetStudentData\x12\x18.ResetStudentDataRequest\x1a\x17.ResetDataStoreResponse2\x80\x05\n\x0e\x43ourseServices\x12;\n\x0c\x43reateCourse\x12\x14.CreateCourseRequest\x1a\x15.CreateCourseResponse\x12;\n\x0cUpdateCourse\x12\x14.UpdateCourseRequest\x1a\x15.UpdateCourseResponse\x12\x45\n\nAddStudent\x12\x1a.AddStudentToCourseRequest\x1a\x1b.AddStudentToCourseResponse\x12R\n\rRemoveStudent\x12\x1f.RemoveStudentFromCourseRequest\x1a .RemoveStudentFromCourseResponse\x12O\n\x0c\x43\x61lculateAve\x12\x1e.CalculateCourseAverageRequest\x1a\x1f.CalculateCourseAverageResponse\x12\x37\n\nGetStudent\x12\x13.GetStudentsRequest\x1a\x14.GetStudentsResponse\x12\x44\n\x0fSetStudentGrade\x12\x17.SetStudentGradeRequest\x1a\x18.SetStudentGradeResponse\x12\x44\n\x0fGetStudentGrade\x12\x17.GetStudentGradeRequest\x1a\x18.GetStudentGradeResponse\x12\x43\n\x0fResetCourseData\x12\x17.ResetCourseDataRequest\x1a\x17.ResetDataStoreResponseb\x06proto3')



_ALLCOURSES = DESCRIPTOR.message_types_by_name['AllCourses']
_COURSE = DESCRIPTOR.message_types_by_name['Course']
_ALLSTUDENTS = DESCRIPTOR.message_types_by_name['AllStudents']
_STUDENT = DESCRIPTOR.message_types_by_name['Student']
_GRADE = DESCRIPTOR.message_types_by_name['Grade']
_GRADE_GRADEENTRY = _GRADE.nested_types_by_name['GradeEntry']
_CREATESTUDENTREQUEST = DESCRIPTOR.message_types_by_name['CreateStudentRequest']
_CREATESTUDENTRESPONSE = DESCRIPTOR.message_types_by_name['CreateStudentResponse']
_UPDATESTUDENTREQUEST = DESCRIPTOR.message_types_by_name['UpdateStudentRequest']
_UPDATESTUDENTRESPONSE = DESCRIPTOR.message_types_by_name['UpdateStudentResponse']
_CREATECOURSEREQUEST = DESCRIPTOR.message_types_by_name['CreateCourseRequest']
_CREATECOURSERESPONSE = DESCRIPTOR.message_types_by_name['CreateCourseResponse']
_UPDATECOURSEREQUEST = DESCRIPTOR.message_types_by_name['UpdateCourseRequest']
_UPDATECOURSERESPONSE = DESCRIPTOR.message_types_by_name['UpdateCourseResponse']
_ADDSTUDENTTOCOURSEREQUEST = DESCRIPTOR.message_types_by_name['AddStudentToCourseRequest']
_ADDSTUDENTTOCOURSERESPONSE = DESCRIPTOR.message_types_by_name['AddStudentToCourseResponse']
_REMOVESTUDENTFROMCOURSEREQUEST = DESCRIPTOR.message_types_by_name['RemoveStudentFromCourseRequest']
_REMOVESTUDENTFROMCOURSERESPONSE = DESCRIPTOR.message_types_by_name['RemoveStudentFromCourseResponse']
_CALCULATECOURSEAVERAGEREQUEST = DESCRIPTOR.message_types_by_name['CalculateCourseAverageRequest']
_CALCULATECOURSEAVERAGERESPONSE = DESCRIPTOR.message_types_by_name['CalculateCourseAverageResponse']
_GETCOURSEREQUEST = DESCRIPTOR.message_types_by_name['GetCourseRequest']
_GETCOURSESRESPONSE = DESCRIPTOR.message_types_by_name['GetCoursesResponse']
_GETSTUDENTSREQUEST = DESCRIPTOR.message_types_by_name['GetStudentsRequest']
_GETSTUDENTSRESPONSE = DESCRIPTOR.message_types_by_name['GetStudentsResponse']
_GETSTUDENTGPAREQUEST = DESCRIPTOR.message_types_by_name['GetStudentGPARequest']
_GETSTUDENTGPARESPONSE = DESCRIPTOR.message_types_by_name['GetStudentGPAResponse']
_SETSTUDENTGRADEREQUEST = DESCRIPTOR.message_types_by_name['SetStudentGradeRequest']
_SETSTUDENTGRADERESPONSE = DESCRIPTOR.message_types_by_name['SetStudentGradeResponse']
_GETSTUDENTGRADEREQUEST = DESCRIPTOR.message_types_by_name['GetStudentGradeRequest']
_GETSTUDENTGRADERESPONSE = DESCRIPTOR.message_types_by_name['GetStudentGradeResponse']
_RESETSTUDENTDATAREQUEST = DESCRIPTOR.message_types_by_name['ResetStudentDataRequest']
_RESETCOURSEDATAREQUEST = DESCRIPTOR.message_types_by_name['ResetCourseDataRequest']
_RESETDATASTORERESPONSE = DESCRIPTOR.message_types_by_name['ResetDataStoreResponse']
AllCourses = _reflection.GeneratedProtocolMessageType('AllCourses', (_message.Message,), {
  'DESCRIPTOR' : _ALLCOURSES,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:AllCourses)
  })
_sym_db.RegisterMessage(AllCourses)

Course = _reflection.GeneratedProtocolMessageType('Course', (_message.Message,), {
  'DESCRIPTOR' : _COURSE,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:Course)
  })
_sym_db.RegisterMessage(Course)

AllStudents = _reflection.GeneratedProtocolMessageType('AllStudents', (_message.Message,), {
  'DESCRIPTOR' : _ALLSTUDENTS,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:AllStudents)
  })
_sym_db.RegisterMessage(AllStudents)

Student = _reflection.GeneratedProtocolMessageType('Student', (_message.Message,), {
  'DESCRIPTOR' : _STUDENT,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:Student)
  })
_sym_db.RegisterMessage(Student)

Grade = _reflection.GeneratedProtocolMessageType('Grade', (_message.Message,), {

  'GradeEntry' : _reflection.GeneratedProtocolMessageType('GradeEntry', (_message.Message,), {
    'DESCRIPTOR' : _GRADE_GRADEENTRY,
    '__module__' : 'scapp_pb2'
    # @@protoc_insertion_point(class_scope:Grade.GradeEntry)
    })
  ,
  'DESCRIPTOR' : _GRADE,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:Grade)
  })
_sym_db.RegisterMessage(Grade)
_sym_db.RegisterMessage(Grade.GradeEntry)

CreateStudentRequest = _reflection.GeneratedProtocolMessageType('CreateStudentRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESTUDENTREQUEST,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:CreateStudentRequest)
  })
_sym_db.RegisterMessage(CreateStudentRequest)

CreateStudentResponse = _reflection.GeneratedProtocolMessageType('CreateStudentResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATESTUDENTRESPONSE,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:CreateStudentResponse)
  })
_sym_db.RegisterMessage(CreateStudentResponse)

UpdateStudentRequest = _reflection.GeneratedProtocolMessageType('UpdateStudentRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESTUDENTREQUEST,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:UpdateStudentRequest)
  })
_sym_db.RegisterMessage(UpdateStudentRequest)

UpdateStudentResponse = _reflection.GeneratedProtocolMessageType('UpdateStudentResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESTUDENTRESPONSE,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:UpdateStudentResponse)
  })
_sym_db.RegisterMessage(UpdateStudentResponse)

CreateCourseRequest = _reflection.GeneratedProtocolMessageType('CreateCourseRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECOURSEREQUEST,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:CreateCourseRequest)
  })
_sym_db.RegisterMessage(CreateCourseRequest)

CreateCourseResponse = _reflection.GeneratedProtocolMessageType('CreateCourseResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATECOURSERESPONSE,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:CreateCourseResponse)
  })
_sym_db.RegisterMessage(CreateCourseResponse)

UpdateCourseRequest = _reflection.GeneratedProtocolMessageType('UpdateCourseRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECOURSEREQUEST,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:UpdateCourseRequest)
  })
_sym_db.RegisterMessage(UpdateCourseRequest)

UpdateCourseResponse = _reflection.GeneratedProtocolMessageType('UpdateCourseResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECOURSERESPONSE,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:UpdateCourseResponse)
  })
_sym_db.RegisterMessage(UpdateCourseResponse)

AddStudentToCourseRequest = _reflection.GeneratedProtocolMessageType('AddStudentToCourseRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDSTUDENTTOCOURSEREQUEST,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:AddStudentToCourseRequest)
  })
_sym_db.RegisterMessage(AddStudentToCourseRequest)

AddStudentToCourseResponse = _reflection.GeneratedProtocolMessageType('AddStudentToCourseResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDSTUDENTTOCOURSERESPONSE,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:AddStudentToCourseResponse)
  })
_sym_db.RegisterMessage(AddStudentToCourseResponse)

RemoveStudentFromCourseRequest = _reflection.GeneratedProtocolMessageType('RemoveStudentFromCourseRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVESTUDENTFROMCOURSEREQUEST,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:RemoveStudentFromCourseRequest)
  })
_sym_db.RegisterMessage(RemoveStudentFromCourseRequest)

RemoveStudentFromCourseResponse = _reflection.GeneratedProtocolMessageType('RemoveStudentFromCourseResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOVESTUDENTFROMCOURSERESPONSE,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:RemoveStudentFromCourseResponse)
  })
_sym_db.RegisterMessage(RemoveStudentFromCourseResponse)

CalculateCourseAverageRequest = _reflection.GeneratedProtocolMessageType('CalculateCourseAverageRequest', (_message.Message,), {
  'DESCRIPTOR' : _CALCULATECOURSEAVERAGEREQUEST,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:CalculateCourseAverageRequest)
  })
_sym_db.RegisterMessage(CalculateCourseAverageRequest)

CalculateCourseAverageResponse = _reflection.GeneratedProtocolMessageType('CalculateCourseAverageResponse', (_message.Message,), {
  'DESCRIPTOR' : _CALCULATECOURSEAVERAGERESPONSE,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:CalculateCourseAverageResponse)
  })
_sym_db.RegisterMessage(CalculateCourseAverageResponse)

GetCourseRequest = _reflection.GeneratedProtocolMessageType('GetCourseRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCOURSEREQUEST,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:GetCourseRequest)
  })
_sym_db.RegisterMessage(GetCourseRequest)

GetCoursesResponse = _reflection.GeneratedProtocolMessageType('GetCoursesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCOURSESRESPONSE,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:GetCoursesResponse)
  })
_sym_db.RegisterMessage(GetCoursesResponse)

GetStudentsRequest = _reflection.GeneratedProtocolMessageType('GetStudentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSTUDENTSREQUEST,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:GetStudentsRequest)
  })
_sym_db.RegisterMessage(GetStudentsRequest)

GetStudentsResponse = _reflection.GeneratedProtocolMessageType('GetStudentsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSTUDENTSRESPONSE,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:GetStudentsResponse)
  })
_sym_db.RegisterMessage(GetStudentsResponse)

GetStudentGPARequest = _reflection.GeneratedProtocolMessageType('GetStudentGPARequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSTUDENTGPAREQUEST,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:GetStudentGPARequest)
  })
_sym_db.RegisterMessage(GetStudentGPARequest)

GetStudentGPAResponse = _reflection.GeneratedProtocolMessageType('GetStudentGPAResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSTUDENTGPARESPONSE,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:GetStudentGPAResponse)
  })
_sym_db.RegisterMessage(GetStudentGPAResponse)

SetStudentGradeRequest = _reflection.GeneratedProtocolMessageType('SetStudentGradeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETSTUDENTGRADEREQUEST,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:SetStudentGradeRequest)
  })
_sym_db.RegisterMessage(SetStudentGradeRequest)

SetStudentGradeResponse = _reflection.GeneratedProtocolMessageType('SetStudentGradeResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETSTUDENTGRADERESPONSE,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:SetStudentGradeResponse)
  })
_sym_db.RegisterMessage(SetStudentGradeResponse)

GetStudentGradeRequest = _reflection.GeneratedProtocolMessageType('GetStudentGradeRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSTUDENTGRADEREQUEST,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:GetStudentGradeRequest)
  })
_sym_db.RegisterMessage(GetStudentGradeRequest)

GetStudentGradeResponse = _reflection.GeneratedProtocolMessageType('GetStudentGradeResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSTUDENTGRADERESPONSE,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:GetStudentGradeResponse)
  })
_sym_db.RegisterMessage(GetStudentGradeResponse)

ResetStudentDataRequest = _reflection.GeneratedProtocolMessageType('ResetStudentDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESETSTUDENTDATAREQUEST,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:ResetStudentDataRequest)
  })
_sym_db.RegisterMessage(ResetStudentDataRequest)

ResetCourseDataRequest = _reflection.GeneratedProtocolMessageType('ResetCourseDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESETCOURSEDATAREQUEST,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:ResetCourseDataRequest)
  })
_sym_db.RegisterMessage(ResetCourseDataRequest)

ResetDataStoreResponse = _reflection.GeneratedProtocolMessageType('ResetDataStoreResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESETDATASTORERESPONSE,
  '__module__' : 'scapp_pb2'
  # @@protoc_insertion_point(class_scope:ResetDataStoreResponse)
  })
_sym_db.RegisterMessage(ResetDataStoreResponse)

_STUDENTSERVICES = DESCRIPTOR.services_by_name['StudentServices']
_COURSESERVICES = DESCRIPTOR.services_by_name['CourseServices']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GRADE_GRADEENTRY._options = None
  _GRADE_GRADEENTRY._serialized_options = b'8\001'
  _ALLCOURSES._serialized_start=48
  _ALLCOURSES._serialized_end=86
  _COURSE._serialized_start=89
  _COURSE._serialized_end=530
  _ALLSTUDENTS._serialized_start=532
  _ALLSTUDENTS._serialized_end=573
  _STUDENT._serialized_start=576
  _STUDENT._serialized_end=818
  _GRADE._serialized_start=820
  _GRADE._serialized_end=907
  _GRADE_GRADEENTRY._serialized_start=863
  _GRADE_GRADEENTRY._serialized_end=907
  _CREATESTUDENTREQUEST._serialized_start=909
  _CREATESTUDENTREQUEST._serialized_end=968
  _CREATESTUDENTRESPONSE._serialized_start=970
  _CREATESTUDENTRESPONSE._serialized_end=1010
  _UPDATESTUDENTREQUEST._serialized_start=1012
  _UPDATESTUDENTREQUEST._serialized_end=1091
  _UPDATESTUDENTRESPONSE._serialized_start=1093
  _UPDATESTUDENTRESPONSE._serialized_end=1133
  _CREATECOURSEREQUEST._serialized_start=1135
  _CREATECOURSEREQUEST._serialized_end=1257
  _CREATECOURSERESPONSE._serialized_start=1259
  _CREATECOURSERESPONSE._serialized_end=1298
  _UPDATECOURSEREQUEST._serialized_start=1301
  _UPDATECOURSEREQUEST._serialized_end=1442
  _UPDATECOURSERESPONSE._serialized_start=1444
  _UPDATECOURSERESPONSE._serialized_end=1483
  _ADDSTUDENTTOCOURSEREQUEST._serialized_start=1485
  _ADDSTUDENTTOCOURSEREQUEST._serialized_end=1551
  _ADDSTUDENTTOCOURSERESPONSE._serialized_start=1553
  _ADDSTUDENTTOCOURSERESPONSE._serialized_end=1598
  _REMOVESTUDENTFROMCOURSEREQUEST._serialized_start=1600
  _REMOVESTUDENTFROMCOURSEREQUEST._serialized_end=1671
  _REMOVESTUDENTFROMCOURSERESPONSE._serialized_start=1673
  _REMOVESTUDENTFROMCOURSERESPONSE._serialized_end=1723
  _CALCULATECOURSEAVERAGEREQUEST._serialized_start=1725
  _CALCULATECOURSEAVERAGEREQUEST._serialized_end=1775
  _CALCULATECOURSEAVERAGERESPONSE._serialized_start=1777
  _CALCULATECOURSEAVERAGERESPONSE._serialized_end=1826
  _GETCOURSEREQUEST._serialized_start=1828
  _GETCOURSEREQUEST._serialized_end=1866
  _GETCOURSESRESPONSE._serialized_start=1868
  _GETCOURSESRESPONSE._serialized_end=1918
  _GETSTUDENTSREQUEST._serialized_start=1920
  _GETSTUDENTSREQUEST._serialized_end=1959
  _GETSTUDENTSRESPONSE._serialized_start=1961
  _GETSTUDENTSRESPONSE._serialized_end=2014
  _GETSTUDENTGPAREQUEST._serialized_start=2016
  _GETSTUDENTGPAREQUEST._serialized_end=2058
  _GETSTUDENTGPARESPONSE._serialized_start=2060
  _GETSTUDENTGPARESPONSE._serialized_end=2096
  _SETSTUDENTGRADEREQUEST._serialized_start=2098
  _SETSTUDENTGRADEREQUEST._serialized_end=2176
  _SETSTUDENTGRADERESPONSE._serialized_start=2178
  _SETSTUDENTGRADERESPONSE._serialized_end=2220
  _GETSTUDENTGRADEREQUEST._serialized_start=2222
  _GETSTUDENTGRADEREQUEST._serialized_end=2285
  _GETSTUDENTGRADERESPONSE._serialized_start=2287
  _GETSTUDENTGRADERESPONSE._serialized_end=2327
  _RESETSTUDENTDATAREQUEST._serialized_start=2329
  _RESETSTUDENTDATAREQUEST._serialized_end=2401
  _RESETCOURSEDATAREQUEST._serialized_start=2403
  _RESETCOURSEDATAREQUEST._serialized_end=2474
  _RESETDATASTORERESPONSE._serialized_start=2476
  _RESETDATASTORERESPONSE._serialized_end=2571
  _STUDENTSERVICES._serialized_start=2574
  _STUDENTSERVICES._serialized_end=2907
  _COURSESERVICES._serialized_start=2910
  _COURSESERVICES._serialized_end=3550
# @@protoc_insertion_point(module_scope)
