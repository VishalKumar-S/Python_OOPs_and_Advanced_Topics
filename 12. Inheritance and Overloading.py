class Parent:
    ''' Inheritance is used to inherit the proeprites of parent to Child. It is also called as "Is-A" relationship" e.g Dog is an animal, This is a vertical relationship between classes. THe 2 main advantages of Inheritance is, COde Reusability and Utilising Exisitng Functionality (for e.,g if Parent has already 10 methods, then child can utilsie the exsitign funcitonlity itself, and creaete new methods,if neceesary, that is not present in the  Parent Class).
    Types of Inheritance:
    Single, Multi-level, Heirarchical, Multiple, Hybrid, Cyclic inheritance
    Java don't support Multiple inheritance. Python suppports all types of inheritance, except Cyclic inheritance, which is not needed.
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

    