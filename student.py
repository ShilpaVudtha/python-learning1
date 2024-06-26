class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students 

    def add_student(self, student):
        if(len.students) < len.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
         value += student.get_grade()
        return value / len(self.students) 

s1 = Student("Tim", 18, 96)
s2 = Student("Jim", 20, 92)  
s3 = Student("Fred", 19, 93)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)


