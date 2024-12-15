class SECE:
    '''I'm outer class'''
    def __init__(self,funds,expenses):
        self.total_funds = funds
        self.total_expenses = expenses
        self.current_director = "Shri.R.Rajaram"
        self.contact_details = self.contact_us(self.current_director)


    def financial_status(self):
        print(f"Funds availabe: {self.total_funds}, Expenses: {self.total_expenses}")

    def update_finances(self,amt):
        self.total_funds-= amt
        self.total_expenses+= amt

    def display_college_details(self):
        print(self.contact_details.__doc__)
        self.contact_details.display()
    
    class Departments:
        '''This {Departments} is an inner class. An inner class is a class, which is declared inside another class. It is done in cases, where without existence of one type of object, there is no chance of existing of another type of object. i.e the inner class would be dependent or associated with the outer class. Without teh outer class, it can;t exist independently
        e.g Outer-inner classes: Car- Engine, Human-Brain, Here,in our case, College - Department, WIthout collefe, department can;t exist indepednedlty, fro eg., if teh college is shut down,then the department can't exist indepednetly,it also would be shut down. Having inner classes increses the modularity of the code '''

        def __init__(self,name, dept_expenses):
            self.dept_name = name
            self.dept_expenses = dept_expenses
            self.courses = ["A","B","C","D","E"]
            self.course_count = 5

        

        def claim_expenses(self):
            try:
                self.update_finances(self.dept_expenses)
            except:
                print("It's Wrong! , inner classes cannot access outer class methods directly without an explicit link to the outer instance. Inner classes in Python are not inherently tied to their outer class instances and don’t inherit anything from the outer class. it's just a class defined inside another class for organizational or logical grouping. There’s no automatic sharing of methods, attributes, or instances between the two classes like inheritance. You need to explicitly pass the outer class instance to make that connection. This approach keeps Python code clean, modular, and explicit. For here, to use the methods of teh outer class SECE, either u need to pass the reference to the outer class object in the constructor of Departments as an instance variable,or pass the ref., varibael as an argumetn to teh claim_expenses seperately")
            
        def claim_expenses_pass_SECE_ref(self, outer_instance):
            outer_instance.update_finances(self.dept_expenses)


        
        def add_courses(self, name):
            self.courses.append(name)
            self.course_count+=1

        class Courses_offered:
            ''' This (Courses_offered) is an nested class here. Here,we can udnerstand teh improtnae of inner classes. i.e if we didnt use any inner classes, then in the outer class SECE itself, we will be forced to have all teh attributes like funds, expenses, dept name,s tudents, faculty count, course credits, code, faculty handled,whihc oworudlnto eb nice., Having inner classes, ameks it better. i.e for e.g, If we need to have  a details about a person ,which also includes his DOB details as dd,mm,yyyy. We'll have the DOB as inner class, the reasons are - since DOB can't exist, if a person does not exist. The next reason is, DOB consists of  3 attributes dd,mm,yyyy. Instaead of having all these attributes along with other person related  attribteus, in teh consturctor of Person outer class itslef, have all the Person realted attirbtues in the outer class as it  is, create  inner class DOB , initialise dd,mm,yyyy ihitn it,adn inteh otuer Person class, call teh DOB inner class, as a instance variable liek e.g, self.dob = self.DOB()'''

            def __init__(self,course_code,credits,course_name, outer_instance):
                self.course_code = course_code
                self.credits = credits
                self.course_name = course_name
                self.access_dept = outer_instance
            

            def update_course_details(self):
                print("Here, we access the outer class., method by creating a instance varibale,which points the ref., variable of the outer Class")
                self.access_dept.add_courses(self.course_name)
            
            
    class ControllerOfExaminations:
        ''' Here, we use nested method insdie a emthod, nested methods,are used ins cenarios,where a specific funcitoanilty within the funciton in needed, repeatabieltiy,so taht if we write tehm out as a nested emthdo,we can reuse them as mcuh we want, instead of writing thema gian and agian, another use case, is when u need to isolate a speerate funciroanlity or logic inside teh funciton, deu to the fact, which is, somehwat nort genralyl used,or any sepfici -use case or funcitaonilty basde, do not want to mix up with the main logic
        Note: There is no nested methods in Java, there are nested methods only in Python'''
        @staticmethod
        def pass_or_fail_calculator():
            def validate_marks(cia_1, cia_2,cia_3,external,assignments,presentation,quiz):
                if cia_1<50 and cia_2<50 and cia_3<50:
                    print("Sorry, u failed,all internal exams, you are not permitted to write the external exams.")
                    return
                
                if external<50:
                    print("Sorry, u failed, in external exam, you didn't pass the exam.")
                    return                            
                
                cia_1 = cia_1*0.08
                cia_2 = cia_2*0.08
                cia_3 = cia_3*0.08

                internal_marks = assignments+presentation+cia_1+cia_2+cia_3+quiz
                if internal_marks<20:
                    print("Sorry u do not have the necessary internal marks")
                    return

                total_marks = internal_marks+external
                if total_marks>50:
                    print("Congrats! You passed the exam")
                else:
                    print("Sorry, u failed the exam")
            
            validate_marks(80,60,90,80,5,5,6)
            validate_marks(10,50,30,60,4,3,5)
            validate_marks(90,60,50,70,4,5,6)
            







    class contact_us:
        ''' To call me, from the outer class SECE, they have created an instance of mine (contact us) and used the instance variable (contact_details) to call me, and execute my methods'''
        def __init__(self, director_name):
            self.curr_director = director_name
            self.phone_no = "+91 4259200300"
            self.e_mail = "sece@sece.ac.in"
            self.location = " Kondampatti [Post], Vadasithur (via), Coimbatore – 641 202, Tamil Nadu, India"
            
        def display(self):
            print("##### Contact Us  #####")
            print("Director Name: ",self.curr_director)
            print("Phone: ",self.phone_no)
            print("e_mail: ",self.e_mail)
            print("Location: ",self.location)


class Bank:
    ''' It is an e.,g to shwo interaction between 2 different classes, how an instance variables of an 1st classs, can be modified by another 2nd class, by craeitng an object of the 1st class, and pass the ref., var of it to the socnd class as parameer, ad modify the require 1st class., instacne variables. We;ll alos here print the diaply funtion of 1st class, by calling it within the second class, with the ref var.,'''

    def sanction_loan(client,loan_amt): 
        ### client acts as self ref., var here
        client.total_funds+=loan_amt
        print("Updated Financial Status of client, after loan approval:")
        client.financial_status()


s = SECE(1000000,25000)
print("Inital funds in college: ",s.total_funds)
print(Bank.__doc__)
Bank.sanction_loan(s,750000)
print(SECE.__doc__)

print("To access, inner classes, from outer classes, we alwasy need to call the classses,to create objects from the top to bottm desired level of inner class")

print(s.Departments.__doc__)
ai_ds = s.Departments("AI_DS",100000)

print("Calling outer class method, from inner class method")

ai_ds.claim_expenses()

print(f"Before: Funds available: {s.total_funds}, Expenses: {s.total_expenses}")

ai_ds.claim_expenses_pass_SECE_ref(s)

print(f"After: Funds available: {s.total_funds}, Expenses: {s.total_expenses}")

print("Calling inner class method, from outer class method")
s.display_college_details()

print(ai_ds.Courses_offered.__doc__)

print("Interaction between inner multi-level classes")

big_data_analytics_course = ai_ds.Courses_offered("R19AD352",4,"Big Data Analytics", ai_ds)

print(f"Before: AI_DS  Courses: {ai_ds.courses}, Count: {ai_ds.course_count}")
big_data_analytics_course.update_course_details()
print(f"After: AI_DS  Courses: {ai_ds.courses}, Count: {ai_ds.course_count}")

pass_or_fail = SECE.ControllerOfExaminations()

print(pass_or_fail.__doc__)
pass_or_fail.pass_or_fail_calculator()







            