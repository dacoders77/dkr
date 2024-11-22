#import pprint

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100

    # Getter
    # Right way to access variables. Do not expose variables as is
    def get_grade(self):
        return self.grade

    # Setter

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

        # When a new student is created, a varuabe of calss Student must be used
        if not isinstance(student, Student):
            raise TypeError(f"Student must be Student class type. Got {type(student).__name__}")

        # Name must be str
        if not isinstance(student.name, str):
            raise TypeError(f"Name must be string type. Got {type(student.name).__name__}")

        # Age must be int
        if not isinstance(student.age, int):
            raise TypeError(f"Age must be int type. Got {type(student.age).__name__}")

        # Grade must be int
        if not isinstance(student.grade, int):
            raise TypeError(f"Student grade must be int. Got {type(student.grade).__name__}")

        print("len: " + str(len(self.students)))

        # self.maxstudents - 1 is because len starts from 0
        if len(self.students) <= self.max_students - 1:
            self.students.append(student)
            return True # If was added properly
        print("Student not added. Limit exceeded")
        return False

    def get_avergae_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


# Create 3 students. Object type of Student
s1 = Student('Boris', 18, 95)
s2 = Student('Jack', 23, 90)
s3 = Student('Gordon', 50, 86)

course = Course('Math', 3)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print("avg grade: " + str(course.get_avergae_grade()))

for student in course.students:
    print(student.grade)