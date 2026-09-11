print("OOP'S in Python ")

class Students:
    # Default constructor
    def __init__(self) :
        print("Default constructor")
        
    # Parameterized constructors
    def __init__(self,name,age):
        print('Constructor of Class Student...')
        self.name = name
        self.age = age
        
    # methods in OOP'S 
    def greetings (self) :
        print("Hello,", self.name)
    
    
    def exams_participants(self) :
        print(f"{self.name} can participate in exams")
    
student_1 = Students("Ali Ahmad", 24)
print("Studnet_1 name : ",student_1.name)
print("Student_1 age : ",student_1.age)
# Creating another student object from the Students class
print("===========================================================================================")
student_2 = Students("Mahad Khan", 26);
print("Studnet_2 name : ", student_2.name)
print("Studnet_2 age : ", student_2.age)
student_1.greetings()
student_2.greetings()
student_1.exams_participants()