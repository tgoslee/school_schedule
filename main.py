from school_schedule.student import Student
from school_schedule.middle_school_student import MiddleSchoolStudent

# first instance
quinn = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )

quinn.add_class("Painting")
quinn.get_num_classes()
quinn.summary()

claire = MiddleSchoolStudent(
                "Claire", 
                "7th Grader", 
                [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ],
                True
            )

# print(claire.get_num_classes())
# print(claire.summary())
# print(MiddleSchoolStudent.mro())

# Extra:
# - create a function that will return the student with more classes
# - create a test for that function