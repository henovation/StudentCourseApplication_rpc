
# Quick start - Hosting on docker
### System requirements:
```
    - python3 (>3.8)
    - docker
    - docker-compose
```
### Run up all services -> Create mock data -> Run tests
```
    docker-compose up
    python3 grpc_app/create_mock.py
    python3 grpc_app/unit_test.py
```
### Use client.py for any other testing [ Inside sc_service container ]
```
    docker exec -it sc_service /bin/sh
    python3 client.py -h
```
#
# Quick start - Hosting on local system (Optional)
### System requirements:
    - python3
    - redis
    - protobuf compiler
### Install redis
```
```
### Run up redis server and open port to 6379
### Install protobuf compiler 
```
```
### Set DOCKER_MODE to False in grpc_app/config.py
### Run up grpc_app server
```
    python3 grpc_app/server.py
```
### Create mock data -> Run tests
```
    python3 create_mock.py
    python3 run_test.py
```
### Use client.py for any other testing
```
    python3 client.py -h
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

```
## Non-functional requirements
```
    * Datastore services should account for async calls and race conditions
    * Datastore rollback feature:
        -- resetDataStore(timestamp) => Default=None, reseting all
    * Unit testing for each function
    * Optimal space/time complexity design
```

