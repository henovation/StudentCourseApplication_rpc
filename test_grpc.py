import pytest
import scapp_pb2 as pb

def test_create_student(grpc_stub):
    value = {
    "student_id": 20,
    "name": "Hello",
    "email": "Hello",
    "credit_capacity": 20,
    "ongoing_courses_id": [
        20
    ]
    }
    request = pb.CreateStudentResponse(message=value)
    response = grpc_stub.Reply(request)

    assert response.message == f'You said: {value}'