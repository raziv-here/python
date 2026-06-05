class Students:
    def __init__(self, Student_Name, Roll_Num, Faculty):
        self.Student_Name = Student_Name
        self.Roll_Num = Roll_Num
        self.Faculty = Faculty

    def full_name(self):
        return f"{self.Student_Name} {self.Roll_Num} {self.Faculty}"
my_Students = Students("Rajib", "004", "Management")
print(my_Students.Student_Name)
print(my_Students.Roll_Num)
print(my_Students.Faculty)
print(my_Students)
print(my_Students.full_name())

#Ihertiance
class GuardianDetails(Students):
    def __init__(self, Student_Name, Roll_Num, Faculty, Guardian_Name, Guardian_Number, Relation):
        super().__init__(Student_Name, Roll_Num, Faculty,)
        self.Guardian_Name = Guardian_Name
        self.Guardian_Number = Guardian_Number
        self.Relation = Relation
    def __str__(self):
        return f"{self.Student_Name} | {self.Guardian_Name} {self.Relation} ({self.Guardian_Number})"
my_student_details = GuardianDetails("Rajib","004", "Management", "Rajan", "Father", "98412222")
print(my_student_details.full_name())
print(my_student_details.Student_Name)
print(my_student_details.Guardian_Name)
print(my_student_details.Relation)
print(my_student_details.Guardian_Number)

#polymorphism= allows us to use a  single interface to represent different funtions
#polumorphism means having forms like one 
#c