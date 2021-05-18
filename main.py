from school_schedule.student import Student
from school_schedule.middle_school_student import MiddleSchoolStudent
from school_schedule.cohort import Cohort

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

student_list = [quinn, claire]
c1 = Cohort("Cohort 1", student_list)
print(c1)

print(c1.class_list("World History"))
print(c1.student_summaries())