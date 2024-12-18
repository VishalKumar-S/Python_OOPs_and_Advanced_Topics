import gc
import time
import sys
###gc module is responsible for garbage collector related methods
class Garbage_Collection:
    ''' An object is considered to be useless, when there is no ref., varibale pointing towards it. i.e., it is not possible to access that object. Garbage collection is useful to remove all these useless objects, if there are too much of these useless objects, and thery ar not destroyed, then it leads to memory constraitn issues, wihihcsops further creation of enw objects.
    In languages like C++, both object creation and garbage collection are manual i,e only the programemr, can create teh objcet, as well as destruct teh object when ther eis no eneed of it. But the programmers, mostly don't destuct the unsued or not needed objects, which leads to memory issesu in C++
    Whereas in langauges like Java, Python, we have automatic as well as manual garbage collection as well. So, when an useless object is dounf i.e where no ref., varibel ispoitnign otoawards teh object, the "garabge collector" will  atuomatically dsestuecs teh objects, leads to no emmroy constraitn issues.
    In python, based on our requirement, we can either enable or disable the garbage collector, with the help of gc module, which is not possuble in Java, makes python special.
    How do u manually make an object, uselesss such that it will be destroeyd by the garbage collector.
    EIther deletet the reg., var., potingin to teh obejct, or point the ref. var to None
    Eg., s = Garbage_Collection()
         Either do,
         i) del s (OR)
         ii) s = None
         in first cae, we deleted teh variabel itself,ins eocnd cae, we just chagning tis potingin toawards.

        Constructor - def __init__()
        Destructor - def __del__():
            Destructor is used, to perform any clean up proceesse in the obecjt, before it's destruction or for any resource re-allocation process for the object.
    
    A garbage collector won;t immediately desturcts an object,when its find it useless. Before destructing any useless object, the garbage collector,will call teh destructor, destructor is repsonsible for ccleanup of the object, like databse connections , netwrok connections with teh object, and freeing up resources,that is consumed by the obejct, only afte executio of desturctor, garbage collector will delete the object.
    Daemon threads are the threads that runs on backgorudn all tiem.Garbage colelctior is an niec e.g, for daemon threads.
    Destructor __del__() in python is same asthte finalise keyword used in Java
    The PVM, is responsible for calling the Garbage collector. Then, then garbage collector is responsible for calling the destructor,it calls the destructor, for clean up purpeos,tehn finally the object is destroyed.
    The destructor is either expleicitely created by hte user, if the usre did not provide the destuctor explcieilty, like Java, in Python also, have teh OBJECT classs, as the parent of all classes,it ahs an default object destructor,which does nothing. Garbage colelctiro is responsibel for exeuttingthe destuctor atumatically. When explcitely destuctor is privide,it exeuted that, whern it si not provide,it used the parent OBJECT class's desturcrotro,which does not do anything. It;s the same for constructors also. IF wedidnt provide explciit constircutor, PVM wil uses the default constructor in the Parent OBject class, whcih does nothign.
    
         '''
    
    def __init__(self):
        print("Im initiating....")

    def __del__(self):
        print("The garbage collector, called thed destructor(me) to clean up the resources, so after i execute, teh garbage collector will destruct the object")
    

print(Garbage_Collection.__doc__)
print("List of attributes, that the default Parent Object Class contains is", dir(object))
print("Is garbage collection enabled?",gc.isenabled())
print("Disable the garbage collector... ")
gc.disable()
print("Is garbage collection enabled?",gc.isenabled())
print("Enable the garbage collector again...")
gc.enable()
print("Is garbage collection enabled?",gc.isenabled())



print("Case 1: ")
t1 = Garbage_Collection()
t1 = None
time.sleep(3)
print("I'm the last line of this program, after i printed, the program will get terminated")
print("Here, removing the ref., var., of the object, will make the Garbage collector immediately  call teh destructor and then destroys the object")


print("Case 2: ")
t1 = Garbage_Collection()
time.sleep(3)
print("I'm the last line of this program, after i printed, the program will now get terminated")
print("Here, even if i didnt remove teh ref pointer, or didnt delete the ref., variable, when the program reaches at it's last, before termination, the Garbage collector will remove all the objects at last, before termnation of teh program, whetehr the object has the ref.,v ar., or not, doesnt matter")


print("Case 3: ")
gc.disable()
t1 = Garbage_Collection()
t1 = None
time.sleep(3)
print("I'm the last line of this program, after i printed, the program will now get terminated")
print("Here, even after being disabling the garabge collector, still the object,whose ref., we marked as None here gets destructed, becuase , in theroy, gc.disable shoudl dsiable teh gabage collector. But in reality, the wroking of gabrage colelctor varies from paltofrm to paltofrm,so only the platofrm,w=inwhcih we wrok,willd ecied whether todisabelt eh gabage colelctor or not. It may ahppend or may not happen")


print("Case 4: ")
gc.disable()
t1 = Garbage_Collection()
time.sleep(3)
print("I'm the last line of this program, after i printed, the program will now get terminated")
print("Here, even after being disabling the garabge collector, still the object gets destructed, even we didnt delete teh ref., to it, becuase , in theroy, gc.disable shoudl dsiable teh gabage collector. But in reality, the wroking of gabrage colelctor varies from paltofrm to paltofrm,so only the platofrm,w=inwhcih we wrok,willd ecied whether todisabelt eh gabage colelctor or not. It may ahppend or may not happen")


print("Case 5: ")
t1 = Garbage_Collection()
t2 = t1
t3 = t2
t4 = t3
del t1
time.sleep(1)
print("Even after deleting t1, object is not destroyed yet, since, t2,t3,t4 are pointing towards the object")
del t2
time.sleep(1)
print("Even after deleting t2, object is not destroyed yet, since, t3,t4 are pointing towards the object")
del t3
time.sleep(1)
print("Even after deleting t3, object is not destroyed yet, since, t4 are pointing towards the object")
del t4
print("Now,i deleted all the ref., variables")
time.sleep(1)
print("Since, here one obejct has 4 ref., variabels,a ll 4 ref,. variables needs to be removed, to make the object useless, to mket he gc to take action")
print("End of Application,I'm the last line")


print("Case 6: ")
li = [Garbage_Collection(),Garbage_Collection(),Garbage_Collection()]
time.sleep(3)
print("The li object is pointed to None now")
li = None
time.sleep(3)
print("Since, here the li is ppitned towards None, all the objects inside li,will get destroyed one by one")
print("Im the last line of execution, Apllication is completed")


print("Find no of ref., variables to an object using sys module methods")
t1 = Garbage_Collection()
t2 = t1
t3 = t2
t4 = t3
print("Here, including all the external 4 ref., pointers, exepclitely mentioned by the programmer, adn icnclduong the implicit self ref., variable provided by the PVM, totally we have ",sys.getrefcount(t1),"ref variables")
print("At last, the program is goign to terminate, im the last line")