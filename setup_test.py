import pytest


@pytest.fixture(scope='module')
def grpc_add_to_server():
    from scapp_pb2_grpc import add_StudentsServicer_to_server

    return add_StudentsServicer_to_server


@pytest.fixture(scope='module')
def grpc_servicer():
    from scapp_pb2_grpc import StudentsServicer

    return StudentsServicer()


@pytest.fixture(scope='module')
def grpc_stub(grpc_channel):
    from scapp_pb2_grpc import StudentsStub

    return StudentsStub(grpc_channel)