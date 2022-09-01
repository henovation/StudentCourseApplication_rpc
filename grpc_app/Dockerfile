# Use the Python3.7.2 image
FROM python:3.8.2-alpine

# Copy the current directory contents into the container at /app
ADD . .
EXPOSE 1024
# Install the dependencies
RUN pip install -r requirements.txt

# Download proto zip
ENV PROTOC_ZIP=protoc-21.5-linux-x86_64.zip
RUN curl -OL https://github.com/protocolbuffers/protobuf/releases/tag/v21.5/${PROTOC_ZIP}
RUN unzip -o ${PROTOC_ZIP} -d ./proto 
RUN chmod 755 -R ./proto/bin
ENV BASE=/usr
# Copy into path
RUN cp ./proto/bin/protoc ${BASE}/bin/
RUN cp -R ./proto/include/* ${BASE}/include/

# run the services
CMD ["python3", "server.py"]
