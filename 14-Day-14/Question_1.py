# Create a class Student that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the averge
class Students :
    def __init__ (self,name,marks):
        self.name = name
        self.marks = marks
         
    def get_average (self) :
        marks = self.marks
        sum =  0
        for i in marks:
            sum += i
        average = sum / len(marks)
        print(f"Hi, {self.name}, Average of your marks {marks[0]}, {marks[1]} and {marks[2]} is = {average}")
student_1 = Students("Abdullah Ahamad", [93,82,79])
student_1.get_average()