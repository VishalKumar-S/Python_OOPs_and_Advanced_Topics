class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

    def add_attr_via_instance_methods(self):
        self.bgrp = "B+ve"

    def delete_inside_class(self):
        print("I'm deleting attributes name and rollno")
        del self.name
        del self.rollno
        print("the current ref var self is",self)
        del self
        try:
            print(self)
        except:
            print("Hey,u have deleted the current ref., var self, which is pointing to the object,so u cant access it ")



s1 = Student("Vishal","22AD122")
s1.add_attr_via_instance_methods()
print(f"No of attributes we have in this objct is,{len(s1.__dict__)}, and it is {s1.__dict__}")

s1.dob = "28/02/2004"
print(f"No of attributes we have in this objct is,{len(s1.__dict__)}, and it is {s1.__dict__}")

del s1.dob
print(f"No of attributes we have in this objct is,{len(s1.__dict__)}, and it is {s1.__dict__}")

s1.delete_inside_class()
print(f"No of attributes we have in this objct is,{len(s1.__dict__)}, and it is {s1.__dict__}")

s2 = Student("x","22ADX")
print(s1)
del s1
try:
    print(s1)
except:
    print(f"you have deleted the ext ref., var., s1, to access the object, so u cant access this current object anymore, but u can aaccess other objecs,sing their respective ref,. var., {s2.__dict__}")
