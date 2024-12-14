class subject:
    '''***This class is used for storing the details of the sibjects*** '''
    x = 10
    # self is used to refer the current object, within the python class, and it is not a sepial keyword, 
    def __init__(self1, name, code, credits):
        print("self ref variable's id is",id(self1))
        self1.name = name
        self1.code = code
        self1.credits = credits
        print("DETAILS:", self1)

    def print_details(self2):
        print("I'm",self2.name,"Code",self2.code,"Credits",self2.credits)


# ref variable
print(subject.__doc__)
s1 = subject("Financial Literacy","R19AD22",3)
s1.print_details()
print("s1's id: ",id(s1))
s2 = subject("History","R19AD22",3)
s2.print_details()
print("s2's id: ",id(s2))


    



