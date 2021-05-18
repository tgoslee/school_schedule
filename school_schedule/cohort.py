class Cohort:
    def __init__(self,name,students):
        self.name = name
        self.students = students

    def student_summaries(self):
        summaries = f"Students in {self.name}: \n"
        for student in self.students:
            summaries += student.summary() + "\n"
        return summaries 

    def class_list(self, class_name):
        students_in_class = []
        for student in self.students:
            if class_name in student.classes:
                students_in_class.append(student.name)
        return students_in_class