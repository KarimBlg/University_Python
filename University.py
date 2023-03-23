class University:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.professors = []
        
    def add_student(self, student):
        self.students.append(student)
        
    def add_professor(self, professor):
        self.professors.append(professor)
        
    def get_students(self):
        return self.students
        
    def get_professors(self):
        return self.professors
    
class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
class Professor:
    def __init__(self, name, department):
        self.name = name
        self.department = department
        
    def get_name(self):
        return self.name
    
    def get_department(self):
        return self.department


university = University("GoldenCollar")

student1 = Student("karim", 17)
student2 = Student("Khaled", 12)
student3 = Student("Hakim", 22)
student4 = Student("Ouerdia", 27)
student5 = Student("Ferroudja", 24)
student6 = Student("Celia", 10)

prof1 = Professor("Bertrand Liaudet", "info")
prof2 = Professor("Amar Assouline", "info")