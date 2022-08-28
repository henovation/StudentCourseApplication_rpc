# Project Description
A backend service system including the API and data store for a StudentCourseAssignment application.
## 1. Architecture and Design
## 2. Functional requirements
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
## 3. Non-functional requirements
```
    * Datastore services should account for async calls and race conditions
    * Whole system should be recoverable in case the application needs to be restarted.
        -- resetDataStore(timestamp) => DataStore should be set to the latest state to that timestamp. (Reset all when timestamp is null)
    * Unit testing for each function
    * Optimal space/time complexity design
```


# Quick Start
## An excel file for generating default data contents. <br>
1. Install dependency
```
    pipenv install -r requirements.txt
```