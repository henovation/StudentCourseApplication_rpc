python3 -m grpc_tools.protoc \
        -I. \
        --python_out=./helper/generated/ \
        --grpc_python_out=./helper/generated/ \
        *.proto