class Association:
    ''' We know that Inheritance is "Is A Relationship". There is another relationship called "Has A Relationship". Composition and Aggregation comes under "Has A Relationship" categorhy e.g, Car Has-A Engine. 
    When 2 things are strongly associated i.e there is no possitibility of existence of contained objects, without the existence of container object, then it's Composition. e.g College Vs Department - College (COntainer), Department (Contained Object). Here, there is no chance of a department can exist without the presence of college. SO, it's compositon.
    When 2 things are weakly associated i.e there is a possitibility of existence of contained objects, even without the existence of container object, then it's Composition. e.g Department Vs Staffs - Department (COntainer), Staffs (Contained Object). Here, even in non -existence of department, staffs can exist. SO, it's Aggregation.
    Examples of Composition - Class and instance variable (Without creating an object of the class, we can't have the instance variable), nested classes are also e.g's of Composition.
    Examples of Aggregation - Class and static variable (even without creating an object of the class, we can have the static variable)
     '''
    
    class Student:
        college_name = "SECE"

        def __init__(self,name):
            self.name = name
            print("Without the class Student, there cannot exist th instance variable Name, makeing it Composition.")









print(Association.__doc__) 
s = Association.Student("Vishal")
print("I don't want to create any Student object, to know the college name. So, it's aggregation", Association.Student.college_name) 
