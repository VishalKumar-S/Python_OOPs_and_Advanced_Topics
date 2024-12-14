class subject:
    ''' In python, if u did not provide constructor to a class, since there is no need of creation of objects in that class, Python provides a default constructor that takes no arguments and does nothing.
    No constructor overloading possible in Python, multipel constructors can present, but only the last constructor will be considered by the PVM '''
    x = 10
    y = 201

    def __init__(self):
        print("Ill not get printed ")

    def __init__(self,x,y):
        self.x = x
        self.y = y

        print("No method overloading possible,only the last constructor will be considered by the PVM, im the last occurence wth the smae method name,os im chosen,so if any object is created usign the parameters, of the previous ocurrence, it will cause errorm, since im the one PVM, wiell consider, so tha method's call should consists of the parameters i have")

    def instance_average(self,x,y):
        print(f"Average is {(x+y)/2} with temporary variables in instance method")

    def instance_average_with_instance_variables(self):
        print(f"Average is {(self.x+self.y)/2} with instance variables in instance method")

    
    @classmethod
    #first argumetn cls
    def class_average(vishal):
        print(f"Average is {(vishal.x+vishal.y)/2} as a class method")


    @staticmethod
    def static_average(x,y):
        print(f"Average is {(x+y)/2} with static decorator as a static method, can be called with either object or class name")

    def static_average_without_Decorator(x,y):
        print(f"Average is {(x+y)/2} without static decorator as a static method, note this is possible only if, this method is called by the class, and not by the object")



s2 = subject(10,100)
s2.instance_average_with_instance_variables()
instance_method = s2.instance_average(10,100)

subject.class_average()

s2.static_average(5,12)
subject.static_average(5,12)
subject.static_average_without_Decorator(5,12)


class Example:
    x = 1
    y = 2
    
    def method(self):
        print("Method with no parameters")
    
    @staticmethod
    def method(x):
        print(f"Method with one parameter: {x}")
    
    @classmethod
    def method(self, x, y):
        print(f"Method with two parameters: {x}, {y}")

e = Example()
e.method(5,5)  # This works
try:
    e.method(1)
except:
    print("It wont work,since no overloading, last method function,with 3 parameters, overrites, all obove smae method names, in python. so u cnat access the method fucntion with 1 attribute")  

try:
    e.method()
except:
    print("It wont work,since no overloading, last method function,with 3 parameters, overrites, all obove smae method names, in python. so u cnat access the method fucntion with no attribute")  