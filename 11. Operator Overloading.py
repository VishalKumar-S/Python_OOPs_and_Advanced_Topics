class Polymorphism:
    ''' Polymorphism means one name, but it has different forms'''
    class Overloading:
        '''Overloading refers to defining multiple functions or operators with the same name, where their parameters differ by type, number, or both. This enables the reuse of same names for different functionalities based on the context and the arguments provided.

        1) Function Overloading:
        marking_scheme(80,90)
        marking_scheme(A,B)
        marking_scheme(80,A,90)
        Note: Python don't have method overloading, whatevr parameter,types, no of paramteres change for the smae fucntion name, Python will only consider the last method of the same named function. Since, there is no datatype explicit mentioning, overloading was not needed for Python.
        
        2)Operator Overloading:
        It enables to use the same operator for whatever objects we want.
        e.,g    'daily_wage+'kumar' = 'daily_wagekumar'
                'daily_wage'*3 = 'daily_wagedaily_wagedaily_wage'
                10+20 = 30

        Note: Java don't support Operator overloading, in Java, although for + operator, alone u can do, arithemtic operatioon,as well as string concatenation i.e 1+2,'a'+'b'. But, other than '+' operator, no other operation, can be used like that, and even + operatro can't be used for any toher purpsoes for our own objects for .e,g object A + obejct B.

        But Operator Overloading, means u can use that operator, for any of your own object's puposes. 
        Python supports Operator Overloading. Here, u can use any operator +,-,>,<=...
        and u can perform operations with any of ur own obejcts like 'a'+'b',1+5, object A + obejct B, object A - obejct B.
        The way,it works, is whenver u use the operator b/w objects, Python uses the magic method of the class, and decide what to do, adn hwatever output that magic metho dof that class Provides, that's going to eb returned as the output for that operation. Magic/Dunder methods are used for Operator Overloading. Here, the methods and their names for each operator  are pre-defined, and we can;t change their names. We need to use them, for our use case

        Example Magic methods:

        Unary Operators: These methods typically take only one argument (the instance itself).

                __neg__(self): Negation (-).

                __pos__(self): Unary plus (+).

                __invert__(self): Bitwise NOT (~).

        Binary Operators: These methods take two arguments (the instance itself and the other operand).

                __add__(self, other): Addition (+).

                __sub__(self, other): Subtraction (-).

                __mul__(self, other): Multiplication (*).

                __truediv__(self, other): Division (/).

                __floordiv__(self, other): Floor Division (//).

                __mod__(self, other): Modulus (%).

                __pow__(self, other): Power (**).

        Comparison Operators: These methods take two arguments (the instance itself and the other operand).

                __eq__(self, other): Equality (==).

                __ne__(self, other): Inequality (!=).

                __lt__(self, other): Less than (<).

                __le__(self, other): Less than or equal to (<=).

                __gt__(self, other): Greater than (>).

                __ge__(self, other): Greater than or equal to (>=).
                
        4. Incremental Operators: Each incremental magic method generally takes one additional argument (the right-hand side operand), while the instance itself (the left-hand side) is implicitly passed as self.

                __iadd__(): +=
                __isub__(): -=
                __imul__(): *=
                __itruediv__(): /=
                __ifloordiv__(): //=
                __imod__(): %=
                __ipow__(): **=
                __iand__(): &=
                __ior__(): |=
                __ixor__(): ^=
                __ilshift__(): <<=
                __irshift__(): >>=       
                
                '''
        class Operator_Overloading:
                '''Whenver we perform operator overloading, the corresponding magic method is called, e.g, ibject A + object B, it's a bianry operator,s o 2 paramters woudl be there ,then we use __add__(self, other)  Here the self instance variable acts, as the 1st operand, whcih is left to teh '+' operator i.e object A, and the other refers to teh 2nd operand, which is in right side of the '+; operator i.e object B. '''

                def __init__(self,value):
                        self.value = value

                def __add__(self,other):
                        return self.value+other.value

                def __sub__(self,other):
                        return Polymorphism.Overloading.Operator_Overloading(self.value-other.value)

                def __ipow__(self,other):
                        return self.value**other.value

                def __mod__(self,other):
                        return self.value%other.value
                
                class modify_str_magic_method:
                        def __init__(self,value):
                                self.value = value
                                        
                        def __add__(self,other):
                                return Polymorphism.Overloading.Operator_Overloading.modify_str_magic_method(self.value-other.value)

                        def __sub__(self,other):
                                return Polymorphism.Overloading.Operator_Overloading.modify_str_magic_method(self.value-other.value)

                        def __str__(self):
                                try:
                                       return "Im printing the value of object a-b-c-a: " + self.value
                                except:
                                       print("It's wrong, It's not Java, in Java only, we can concatenate  a string with an integer, in Python, we can concatenate a string with only another string, We can't concatenate  a integer with a string, here value is an integer.So,we wodl modify it as")
                                       return "Im printing the value of instance object a-b-c-a: "+ str(self.value)
                        



      


p = Polymorphism()
op = p.Overloading()
print(p.__doc__)
print(op.__doc__)
print(op.Operator_Overloading.__doc__)
print("You can find all teh avilbe magic emthod,of ur data type uisng, ",dir(int))
a = op.Operator_Overloading(2)
b = op.Operator_Overloading(10)
a**=b
print("Operated with incremental operation",a)
try:
        print(a%b)
except:
        print("It won;t work, since preivosuly we did in-place pow func., and modfied a,in place and we retuned it as an integer, not as an object. So,now a is an itnerger , b is still an object, int+object=>typeError")
        print("we'll make them object again")
        a = op.Operator_Overloading(2)
        print("Now,it works",a%b)

try:
        c = op.Operator_Overloading(17)
        print(a+b+c)
except:
        print(f"Type of a+b: {type(a+b)}, c: {type(c)}")
        print("It won;t work, since a+b returns integer, c is an object, Int + Object, returns an type error,it can't perform the operation. To perforom a+b+c, the magic method considers all the operands before the last operator sign as self argument, and the right side operand as the otehr argumetn i.e (a+b)+c, so what we do is, instead of just return self.a+self.b for a+b, which is just an integer, we are going to return it as an Operator_Overloading class Object. For demonstration, here we will not be creating the __add__() method with the return type of object, since ther is no method overloading in python, it will only execute the last ocurence of the __add__() method, then if it eecutes the last __add__(), which returns as object, then it would be used, for teh privsou e.,gs as well, the preivosu int returning __add__() would be ignored. So, all ou r previous e.g., would not make sense., So, instead of add,we do __sub__() whih returns teh result as object")
        print("The type of a+b is",type(a+b))
        print("The type of a-b is",type(a-b),"here, a-b will be computed in the __sub__(), and a new object is created, and the constructor's value fo this obejct becomes this resultant a-b, and we return this object")
        print("So, now u can use as much operands fro ur arithemtic oeparitosn,it executes wihttu any issues, sicne here all the return value fo operations woule be objects, no isseues  a-b-c-a = (a-b-c)-a = obj+obj=>")
        print(a-b-c-a)
        print(type(a-b-c-a))
        print("So, to make the a-b-c-a returned object to print the resultant a-b-c-a value, instead of the object name, we are going to modify the magic method __str__(). The reason is, whenever,In Python, when you use the print() function, it internally calls several methods to handle the output. Here's a high-level overview of the process: Internal Mechanisms of print():Like Java,if we try to print the ref., var., there it calls the .tostring() method, in Python, when we try to print the ref., var., it calls the default __str__() magic method of the object class,, which prints, the object iterator string. print() Function in Python: The print() function is a built-in function in Python that converts its arguments to a string and outputs them to the standard output (usually the console). __str__ and __repr__ Methods: For each object passed to print(), Python first tries to call the object's __str__() method to get its string representation. If the object does not have a __str__() method, Python falls back to the __repr__() method. So,here we are going to override the defaukt __str__() with our our implementation. Sp, python will consider only ours, it won't consider the default __str__(), now, when we try to print, it will print the correct a-b-c-a value. Note, that we are going to createa new inner class inside teh Operator Overrifing class, and modify the __str__(method) there, not within this class,the reaon of it, is all teh print statements i used here, before this print statemnts,is of the same level scope of class Operator_Overloading, if we do override the __str__  here itself, then all the previous print statementes, when get executed, isntead of them eecuting their defautl __str__,it will be using our overrided one, whcih we doing it only fo thi specific a-b-c-a, so ti will afffect the outptu fo thepreivsu output stamtens,")
        a = op.Operator_Overloading.modify_str_magic_method(2)
        b = op.Operator_Overloading.modify_str_magic_method(10)
        c = op.Operator_Overloading.modify_str_magic_method(17)
        print("Our type of resultant operation with our new version of magic methods",type(a-b-c-a))
        print(a-b-c-a)
        print("So, now we made to print the resultant value, instead of the object, by our overriding")


class wage:
        ''' Performing operator overloading across different classes'''
        def __init__(self,p,w):
                self.person = p
                self.wage = w
        
        def __mul__(self,other):
                return self.wage*other.days
        
class days:
        def __init__(self,p,d):
                self.person = p
                self.days = d

        def __mul__(self,other):
                return self.days*other.wage

print(wage.__doc__)
daily_wage = wage("Vishal",5000)
Worked_days = days("Vishal",30)
print("To multiply worked days and the salary, ans id u need to get the salary,even when u print in either of these ways, daily_wage*Worked_days or Worked_days*daily_wage, then u need to write the __mul__() in both of the classes, or if u just want to print salary using daily_wage*Worked_days, having __mul__() in only wage class is enough or if u need to print salary using Worked_days*daily_wage, having __mul__() in only wage class is enough, but if u try to print on the other way i.e in reveser,it throws erro, since Python checks whether the first argument's class having tha mul magic method or not,if tt's not over there,it immediately returns error ")
print("My salary:", daily_wage*Worked_days)
print("My salary:", Worked_days*daily_wage)
        



      

