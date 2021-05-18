from .student import Student

class MiddleSchoolStudent(Student):
    def __init__(self,name,grade,classes,transportation):
        # self.name = name
        # self.grade = grade
        # self.classes = classes
        super().__init__(name,grade,classes)
        self.transportation = transportation
    
    # def summary(self):
    #     if self.transportation == True:
    #         return f"{super().summary()} Eligible for transportation!"
    #     else:
    #         return f"{super().summary()} NOT eligible for transportation!"