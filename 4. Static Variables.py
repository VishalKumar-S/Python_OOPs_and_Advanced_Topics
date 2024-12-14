class Student:
    c_name =  "SECE"
    def __init__(self):
        self.year = 2026
        Student.year = 2022


    def instance_method(self):
        Student.place = "Coimbatore"

    @classmethod
    def class_method(cls):
        Student.birth_date = "28/02/2004"
        cls.dob = "28/02/2004"
        print("Accessing static var inside the class using cls",cls.birth_date)

    @staticmethod
    def static_method():
        Student.color = "Blue"

    def access_static_variables(self):
        print("Accessing static var inside the class using Class name",Student.birth_date)
        print("Accessing static var inside the class using self", self.birth_date)
    
    @classmethod
    def modify_static_variables(cls):
        Student.birth_date = "04/04/2004"
        cls.color = "Red"
    
    @classmethod
    def delete_static_variables(cls):
        del cls.color
        del Student.place
        


t = Student()
Student.c_full_name = "Sri Eshwar College of Engineering"
print("Declared in the top of class",Student.c_name)

print("Declared using class name outside the class using class name, cant be done using instance variables", Student.c_name)
print("Declared Static variable using constructor,it will not print 2026,since that year variable is a instance varibael , not static variable",Student.year)

t.instance_method()
print("Declared static variables using instance methods",Student.place)
t.class_method()
print("Declared static variables using class name in class method",Student.birth_date)
print("Declared static variables using class method's cls ref variable",Student.dob)
t.static_method()
print("Declared static variables using static method",t.color)

print("Accessing static variables using class name outside the class",Student.color)
print("Accessing static variables using ref variable outside the class", t.color)

t.access_static_variables()

Student.c_name = "School"
print("Modified static variable outside the class using class name, from SECE to,",Student.c_name)

t.c_name = "AMS"
print(f"t.c_name creates new instance variable c_name = AMS, it won't modify the class-level static variable, c_name static variable c_name: {Student.c_name}, instance's c_name: {t.c_name} ")
t.modify_static_variables()
print(f"Modified  birth_date and color to {Student.birth_date} and {Student.color} using cls and class name inside the class")


t.delete_static_variables()
del Student.year
try:
    print(t.color)
    print(Student.dob)
    print(Student.year)
except:
    print("Deleted color and place inisde the class using class name and cls, year using class name outside the class, so we can't access them now")


print("Final class attributes",Student.__dict__)