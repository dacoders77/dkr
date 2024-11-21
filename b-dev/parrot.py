class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100

    # Getter
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = [] # List
        self.is_active = False

    def add_student(self, student):
        # Add validation and make sure that all variables have correct format
        #print(type(student).__name__)
        #exit()

        print ("add_student method called")

        if not isinstance(student, Student):
            raise TypeError(f"Student must be an integer. Got {type(student).__name__}")

        if not isinstance(student.grade, int):
            raise TypeError(f"Student grade must be int. Got {type(student.grade).__name__}")

        if len(self.students) < self.max_students:
            self.students.append(student)
            return True # If was added properly
        return False

    def get_avergae_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


s1 = Student('Boris', 18, 95)
s2 = Student('Jack', 23, 90)
s3 = Student('Gordon', 50, 86)

course = Course('Math', 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
print(course.get_avergae_grade())



