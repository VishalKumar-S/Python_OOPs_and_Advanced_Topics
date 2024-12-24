class Parent:
    ''' Inheritance is used to inherit the proeprites of parent to Child. It is also called as "Is-A" relationship" e.g Dog is an animal, This is a vertical relationship between classes. THe 2 main advantages of Inheritance is, COde Reusability and Utilising Exisitng Functionality (for e.,g if Parent has already 10 methods, then child can utilsie the exsitign funcitonlity itself, and creaete new methods,if neceesary, that is not present in the  Parent Class).
    Types of Inheritance:
    Single, Multi-level, Heirarchical, Multiple, Hybrid, Cyclic inheritance
    Java don't support Multiple inheritance. Python suppports all types of inheritance, except Cyclic inheritance, which is not needed for use, so not provided by both languages.
'''

    def wealth(self):
        print("Money, Land, Investments")

    def child_education(self):
        print("My son will be a Maths Guy")


class Child(Parent):
    ''' You can inherit as much classes u want like class Child(P1, P2, P3....)
    '''

    def child_education(self):
        print("If u don't want to inherit ur parents wish of becoming a math guy, then u can override, ur parents wish and become ML engineer. Here, we overrided the child_Education() of parent. In Overriding, the parameter dont matter, jsut wr ened to check both the method names are same or not.")
        super().child_education()
        print("I will become a ML Engineer")

    
 
print(Parent.__doc__)
print(Child.__doc__)
c = Child()
print("IF u wanat to inherit ur parents proeprties,")
c.wealth()

print("Although u inherit wealth fromur parent, u dont want to inherit theri wihs of ur educaiton, so u can Override, just use the smae emthod name adn say ur wish. But if u think u also want to inherit ur parents wish , as weela s ur, then use super() to inherit ur parentrs, as wella s overriding to use ur wish")
c.child_education()


class G:
    def a(self):
        print("I'm Grand-Father")

class P(G):
    def b(self):
        print("I'm Father")

print("### 1. Single Inheritance: 1 parent, 1 child")
s = P()
s.b()
s.a()

class C1(P):
    def c1(self):
        print("I'm child 1")


print("### 2. Multi-level Inheritance: Implementing single inheritance at multiple levels")
s = C1()
s.c1()
s.b()
s.a()

class C2(P):
    def c2(self):
        print("I'm child 2")

print("### 3. Heirarchial Inheritance: 1 parent, multiple children at same level")
s = C2()
s.c2()
s.b()
s.a()
try:
    s.c1()
except:
    print("It throws error, since C1 and C2 are at the same level, and C2 inherits only from the parent, not from his another sibling")


print("### 4. Multiple Inheritance: Multiple parents, 1 children")
print("We face ambiguity or diamond access problem in Java, so only Multiple inheritance not possible. i.e if child inherits from 2 parents P1 and P2, and if both P1 and P2 consists of the same method, then Child dont know which one to use, causing issue. SO,it was excluded. But in python,it supports Multiple inheritance, by method resolution. It chooses the mthod, of the class, which is inherited first i.e based on the order of teh parents inheited,it calls the method")

class P1():
    def parent(self):
        print("Im his parent (Father)")

class P2():
    def parent(self):
        print("Im his parent (Mother)")

class C1(P1,P2):
    def child(self):
        print("Im their first child")

class C2(P2,P1):
    def child(self):
        print("Im their second child")

class C3(P1,P2):
    def child(self):
        print("Im their third child")

    def parent(self):
        print("P1 and P2 are my parents")

s = C1()
s.child()
s.parent()
print("Here, the parent father gets printed, instead of mother, since the order of the inheritance, P1 stands first before P2. P2 will only be reviewed for method parent(), only if there is no parent() in C1 as well as P1")

s = C2()
s.child()
s.parent()
print("Here, the parent mother gets printed, instead of father, since the order of the inheritance, P2 stands first before P1. P1 will only be reviewed for method parent(), only if there is no parent() in C2 as well as P2")


s = C3()
s.child()
s.parent()
print("Here, the parent() of child gets printed, since why need to check the methods of parent classes, when the child already has that method. So, here the child's parent() method will be only used.")



print("### 5. Hybrid Inheritance: Has 2/more than 2 different types of inheritance combined. It coudl be anything from a single to multiple levels, to single or multople parents, children etc.,")


print("### 6. Cyclic Inheritance: It is not needed for use, so most of the programming languages don't support it")

try:
    class A(A):
        pass

except Exception as e:
    print("We'll face the error",e,"here, since there is no point of inheriting properitties of class A, by class A itself, so Python shows error")



try:
    class A(B):
        pass

    class B(A):
        pass

except Exception as e:
    print("We'll face the error",e,"here, if class A, wants to inherit all the proerpties of class B, ans class B,wants to do the same vice versa, why to have 2 seperate classes, instead have one single class itself, combining both")




