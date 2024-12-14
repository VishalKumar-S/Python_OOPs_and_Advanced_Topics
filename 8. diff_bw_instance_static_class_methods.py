class difference:
    '''Instance methods are costlier than class methods, since self ref., variable is passed. So, do not use instance methods, if u do not have any instance var., isntead go for static variables'''

    def static_method(x,y):
        print("Static varaibles are not related to staic methods, static variables are used in class-methods as class-level variables, static methods are general utility methods or helper methpds")
        print(x+y)  
    

    def whatif(cls,self):
        cls.x = 10
        print("Here, clas x {} acts as a self ref variable, and the seond apramter self acts as a nnormal argument,since Python dont have specific keyword, only the positon of the argumetn is considered, since cls is teh first postiion, it owudl eb act as the self varaible. Thus, we are using an instance method whatif, to assign a enw instance variable x, using the ref., variable cls and print the name variable,self".format(cls.x).
        )

        print("Hi,I am ",self)



print(difference.__doc__)
difference.static_method(1,2)
s = difference()
s.whatif("Vishal Kumar. S")