class human():
    ''' super() method is to invoke the parent class method, by the child class method, for the purpose of child class. Maina dvantage of using it is COde reusability. Instead of writing the same common code,again and agian in the child class, we can initlaise it in the parent class,adn use super to use it. When the child inherits multiple parents, and all those parents have the same method name, then super will order the MRO algorithm to choose the correct method class. But if u  need to call a specific parent's method, instead fo floowing the MRO order of the method lookup,htere are 2 ways to call specific parent;s method name.
    1. parent_Class_name.method_name(self) 
    2. super__(Class_name, self).method_name() Here it won't call the method of class_name, scine we used super(), it goes the the parent of the class_name adn uses that's method.
    
    When you use super(), you're working with the parent class's methods and class variables, but NOT directly with instance variables. Instance variables are always bound to self.
    '''

    no_of_hands = 2
    no_of_legs = 2

    def face(self):
        self.face_shape = 'Oval'

    def __init__(self,name,age):
        print("You are using human construcotr")
        self.name = name
        self.age = age
        self.eyes = 2

        print(name,age)
    
    def display(self):
        print("Display function of human")
        print("Name: ",self.name)
        print("Age: ",self.age)

    @staticmethod
    def static_method():
        print("Im parent static method")

    @classmethod
    def class_method(cls):
        print("Im parent class method")

    def instance_method(self):
        print("Im parent instance method")



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
        print(f"I can use static/class variables of parent within child, with just using super().I have {super().no_of_hands} hands and {super().no_of_legs} legs")
        print(f"I have {self.eyes} no of eyes. eyes is an instanve variable in the constructor of the human class. So,to access it we need to have self, can't do with super()")
        try:
            print(super().face_shape)
        except Exception as e:
            print("Error is ",e,"The reason is, u can't call a parent class instance variable directly, using super() in child class, u need to use self")
            try:
                print("My face shape is",self.face_shape)
            
            except Exception as e:
                print("The error is ",e,"When you use super(), you're working with the parent class's methods and class variables, but NOT directly with instance variables. Instance variables are always bound to self. If the face_shape var., was within the constructor, the face_type var., woudl have been initlaited automatically, when we r using the our self, we would have used it directly, but here face() is an instance method. So, we would need to call the instance method to initialise the instance_varibale")
                self.face()
                print("My face shape is",self.face_shape)
            
    @staticmethod
    def static_method():
        print("Im child static method,trying to access parent's satic,class and instance methods")
        try:
            super().static_method()
            super().class_method()
        except Exception as e:
            print("Error is",e,"The error RuntimeError: super(): no arguments occurs because the super() function requires information about the class and instance from which it is called, which it cannot infer in a static method. In a static method, there's no automatic way to get the current class or instance because static methods don't receive self or cls as parameters.")
            human.static_method()
            human.class_method()
            print("OR")
            super(Teacher,Teacher).static_method()
            super(Teacher,Teacher).class_method()

        try:
            super().instance_method()
        except Exception as e:
            print("Error is,",e,"You cannot call a instance method without self. If u want to call the isntance method wihitn static method, u need to pass teh ref., var explicitely to this staic method to call the instance method")
            human.instance_method(Teacher("Durga", 40, "Python", 10))



    @classmethod
    def class_method(cls):
        print("Im child class method,trying to access parent's satic,class and instance methods")

        print("When you call super() in a class method, you can use cls to provide the class context, and it will resolve the method based on the MRO.")
        super().static_method()
        super().class_method()


        print("OR")
        super(cls,cls).static_method()
        super(cls,cls).class_method()

        try:
            super().instance_method()
        except Exception as e:
            print("Error is,",e,"You cannot call a instance method without self. If u want to call the isntance method wihitn class method, u need to pass teh ref., var explicitely to this staic method to call the instance method")  
            print("here, it is how: ")
            super(Teacher,cls("Durga Sir",40,"Python",10)).instance_method()
            print("OR")
            human.instance_method(cls("Durga Sir",40,"Python",10))

    def instance_method(self):
        print("Im child instance method,trying to access parent's satic,class and instance methods")    
        super().instance_method()
        super().static_method()
        super().class_method()
      
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
t.static_method()
t.class_method()
t.instance_method()
s = Student("Vishal",20,'III')
s.display()
