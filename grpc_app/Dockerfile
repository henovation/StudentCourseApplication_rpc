# Use the Python3.8.2-alpine image
FROM python:3.8.2-alpine

# Copy the current directory contents into the container at /app
ADD . .
EXPOSE 1024

# Install protobuf
RUN unzip -o /proto/protoc-21.5-linux-x86_64.zip -d ./proto
RUN chmod 755 -R ./proto/bin
ENV BASE=/usr
# Copy into path
RUN cp ./proto/bin/protoc ${BASE}/bin/
RUN cp -R ./proto/include/* ${BASE}/include/

# Install the dependencies
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

# run the services
CMD ["python3", "server.py"]
