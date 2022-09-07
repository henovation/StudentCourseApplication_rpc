
# Quick start - Hosting on docker
### System requirements:
```
    - python3.8 
    - docker
    - docker-compose
```
### Run up all services
```
    docker-compose up

```
### [ Inside sc_service container ] Create mock_data -> Run unit_test -> Use client.py for any other testing 
```
    docker exec -it sc_service /bin/sh
    python3 create_mock.py
    python3 unit_test.py
    python3 client.py -h
```
### [ Inside redis_backup container ] Setup backup schedule for restoring purpose
```
    docker exec -it redis_backup /bin/bash
    chmod +x ~/redis_backup.sh
    crontab -e
    */5 * * * * ~/redis_backup.sh
```

#
# Quick start - Hosting on local system (Optional)
### System requirements:
    - python3
    - redis
    - protobuf compiler
### Install redis
```
    https://redis.io/docs/getting-started/installation/
```
### Run up redis server and open port to 6379
### Install protobuf compiler 
```
    https://grpc.io/docs/protoc-installation/
```
### Set DOCKER_MODE to False in grpc_app/config.py
### Install dependency
```
    python3 -m pip install --upgrade pip
    python3 -m pip install -r grpc_app/requirements.txt
```
### Run up grpc_app server
```
    python3 grpc_app/server.py
```
### Create mock data -> Run tests
```
    python3 grpc_app/create_mock.py
    python3 grpc_app/unit_test.py
```
### Use client.py for any other testing
```
    python3 grpc_app/client.py -h
```
#
# Project Description
A backend service system including the API and data store for a StudentCourseAssignment application.


## Functional requirements (Exposed APIs)
```
    1.createStudent(Student s) -> Boolean // true if succeed else false
    2.updateStudent(Student s) -> Boolean // true if succeed else false
    3.createCourse(Course c) -> Boolean // true if succeed else false
    4.updateCourse(Course c) -> Boolean // true if succeed else false
    5.addStudentToCourse(Student s, Course c) -> Boolean // true if succeed else false
    6.removeStudentFromCourse(Student s, Course c) -> Boolean // true if succeed else false
    7.calculateCourseAverage(Course c) -> Double // A – 5, B – 4, C – 3, D – 2, F – 0
    8.getCoursesOfStudent(Student s) -> List<Course>
    9.getStudentsOfCourse(Course c) -> List<Student>
    10.getStudentGrade(Student s, Course c) -> String // “A”, “B”, “C”, “D”, “F”
    11.getStudentGradePointAverage(Student s) -> Double // A – 5, B – 4, C – 3, D – 2, F – 0
    12.resetDataStore(Long timestamp) -> Boolean // true if succeed else false
    13.setStudentGradeForCourse(Student s, Course c, String grade) -> Boolean // true if succeed else false
    14.the static main(String[] args) function will call each of the functions listed to demonstrate how each function can be used.
```

## Functional requirements (dev/debug use)
```
    1.list_all_students() -> List of Student
    2.get_studentList() -> Dictionary of all students' name and ID
    3.list_all_courses() -> List of Course
    4.get_courseList() -> Dictionary of all courses' name and ID
    5.get_student_by_id(Int studentId) -> Student 
    6.get_course_by_id(String courseId) -> Course
    7.create_student_by_input() -> manual input from commad line
```
## Non-functional requirements
```
    * Datastore services should account for async calls and race conditions
    * Datastore rollback feature:
        -- resetDataStore(timestamp) => Default=None, reseting all
    * Unit testing for each function
    * Optimal space/time complexity design
```

