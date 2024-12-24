class human():
    ''' super() method is to invoke the parent class method, by the child class method, for the purpose of child class. Maina dvantage of using it is COde reusability. Instead of writing the same common code,again and agian in the child class, we can initlaise it in the parent class,adn use super to use it. When the child inherits multiple parents, and all those parents have the same method name, then super will order the MRO algorithm to choose the correct method class. But if u  need to call a specific parent's method, instead fo floowing the MRO order of the method lookup,htere are 2 ways to call specific parent;s method name.
    1. parent_Class_name.method_name(self) 
    2. super__(Class_name, self).method_name() Here it won't call the method of class_name, scine we used super(), it goes the the parent of the class_name adn uses that's method'''

    def __init__(self,name,age):
        print("You are using human construcotr")
        self.name = name
        self.age = age
    
    def display(self):
        print("Display function of human")
        print("Name: ",self.name)
        print("Age: ",self.age)

class School_members(human):
    def __init__(self,school_name,id_no, bus_no):
        print("You are using School_members construcotr")
        self.school_name = school_name
        self.id_no = id_no
        self.bus_no = bus_no


    def display(self):
        print("Display function of School members")
        print("Name: ",self.name)
        print("Age: ",self.age)


class Teacher(human):
    ''' Here in teacher class, instead of me re-writing the name and age re-initalsiign in the constructor, i woudl rather call super() to use my parents instance variables. FOr display function also, I'll use my Parent's  existing common part, enabling code reusability'''
    def __init__(self,name,age,subject,experience):
        super().__init__(name,age)
        self.subject = subject
        self.experience = experience

    def display(self):
        super().display()
        print("Subject: ",self.subject)
        print("Experience: ",self.experience)
      
print(human.__doc__)

try:
    class Student(human,School_members):
        pass

except Exception as e:
    print("The error is ",e, "The reason is, Student tries to inherit from human, then School members. School Members local precendence order, is to check School_Mmebrs, then only Human, thus violating this principle. SO, Python don't knwo the correct MRO oder of it, creating conflict")
    print("MRO of Student = [Student] + Merge(MRO(human), MRO(School_members), [human, School_members])\nMRO of Student = [Student] + Merge([human, object], [School_members, human, object], [human, School_members])")

    print("SO, either use Student(School_members,human) or simply Student(School_members) as school_members already inherits from the Human class")    




class Student(School_members):
    def __init__(self,name,age,grade):
        print("Student's MRO order is: ",Student.mro())
        try:
            super().__init__(name,age)
            self.grade = grade
        except Exception as e:
            print("It throws the error",e,"Since, the MRO order looks up the __init__() of school_members, and ther is argument mismathc ebtween both, leads to error.")
            print("you can resolve it, by instead of calling the constructor of school_memebr,s call teh construcotr of Human,itself as it's already in multi-levl inheritane structure i.e human is laredy inherited by school_members")
            human.__init__(self,name,age)
            self.grade = grade

    

    def display(self):
        print("let us print the student details with our prefeered parent's methods")
        print("1. Displaying the details via using school_members's display()")
        super().display()
        print("Grade: ",self.grade)
        print()
        print("2. Displaying the details via using human's display()")
        super(School_members,self).display()
        print("Grade: ",self.grade)




print(Teacher.__doc__)
t = Teacher("Shreekanth Verma Chekuri",40,'ML',10)
t.display()
s = Student("Vishal",20,'III')
s.display()
