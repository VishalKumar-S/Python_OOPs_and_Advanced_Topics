x = 800
class Student:
    x = 700
    global name
    name = "Vishal"

    def with_local_and_gloal_variable(self):
        try:
            print("Im printing global variable x,since i didnt have any local variable x",x)

        except:
            print("It's wrong, x = 800 is declared at the global level. Inside functions, unless explicitly declared as global x, any assignment to x will create a local variable. Python assumes x is local because x = 805 is assigned later in the same function.. However, before this assignment, x is accessed, causing an UnboundLocalError because the local x is not yet initialized. This is why the except block executes with the explanation.. Global Variable Access works unless a local variable with the same name is created in the function (here it is done, below x = 805). Declare global x inside the function to explicitly use the global x. ")

        x = 805
        print("Im printing local variable x,since now local variable is given prefernece, not global variable, x = ",x)



    def with_global_variable(self):
        print("Im printing global variable x,since i didnt have any local variable x",x)

    def with_local_variable(self):
        x = 50
        y = 7561
        print("Im printing local variable x,since now local varibale is given prefernece, not global variable",x)
    
    def access_local_variable(self):
        try:
            print(y)
        except:
            print("I can't access y, since it's a local varibale of the with_local_and_gloal_variable() function")

    def with_static_Variable(self):
        print("I'm printing static variable, it can be accesse uisng both calss name,as wella as ref varibale",self.x)
    
    def global_Var_inside_Class(self):
        global y
        y = 7561
    
    def accessing_global_Variables(self):
        print("Now i can access y,since it's now a global variable,e evn though its declared within global_Var_inside_Class function",y)

    def access_global_var_dec_inside_class(self):
        print("Accessing global varibale declared inside the class",name)    

t = Student()
t.with_local_and_gloal_variable()
t.with_global_variable()
t.with_local_variable()
t.access_local_variable()
t.with_static_Variable()
t.global_Var_inside_Class()
t.accessing_global_Variables()
t.access_global_var_dec_inside_class()
print("GLobal variable x is",x)
print("Class variable x is",t.x)

    
