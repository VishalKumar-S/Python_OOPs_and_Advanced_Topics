from threading import *
import time
print("Multi-tasking: Executing different tasks simultaneously. 2 types: \n 1) Process-based Multi-tasking: Multiple tasks execute simultaneously, where each task is an independent process with it's own memory space. Process-based multi-tasking is the most used concept, at the operating system level.  \n 2) Thread-based Multi-tasking: Multiple tasks execute simultaneously, where each task is an independent part of the same program, and share the same memory space. Thread-based multi-tasking is the most used concept, at the application level.\n A thread is an: \n 1) Independent part of a program \n 2) It is considered as a flow of execution. \n 3) It is a python object \n For every thread, independent job is available. Whrever indedependednt jobs are available, multi-threading is best suited,as it provides better performance.\n in generally, every web server contains 60 threads. So, at a time, 60 client requests can be handled by the server simultaneodsuly. But,it can be icnreasesd/decreased, abed on our demand. After client requests completed, thread will be allocated to the next request \n. By default PVM, contains a single thread running, which is the main thread. We can sue threading library to do threading operations. For every thread, PVM assigns a unique identification no")

print("Current running thread Name",current_thread().name)

print("There are 3 ways to create a thread: \n 1) Create a thread without using any class. \n 2) Create a thread extending the Thread class. \n 3) Create a thread, without extending the Thread Class.\n")

print("1) Without extending any class: (Functional Programming Way)")
def display():
    for _ in range(10):
        print("I'm a child thread: ",{current_thread().name})

t = Thread(target = display)
list_of_threads = enumerate()
print("\nList of active threads by default: ")
for thread in list_of_threads:
    print(f"Thread Name: {thread.name}, Thread ID: {thread.ident}")
print("\n")

print("Main thread will create the child thread, after start().Now, well have 2 threads, and both will execute simulataneously")
t.start()
list_of_threads = enumerate()
print("\nList of active threads after i create another thread for our display function: ")
for thread in list_of_threads: 
    print(f"Thread Name: {thread.name}, Thread ID: {thread.ident}")
print("\n")




for _ in range(10):
    print("I'm a parent thread: ",{current_thread().name})

print("here, this parent thread printing statemtn is executed by the main thread, adn dsiplay() is executed by the chidl thread. Both threads execute simultaenously, we cant't predict the exact order in which they will print, but it is of no issue, since we only use multithreading fro 2 processes wehihc are independent, i.e their order of in between executions dont matter, since we wont care about the task, only about hte job being done. ID bth processes are dependent in case,then order is impo., over there, then we won;t use multithreading over there\n")


print("2) Extending the Thread class: (OOPs Way)")

class child(Thread):
    def run(self):
        for _ in range(10):
            print("CHILD THREAD STATEMENT: I'm a child thread:",current_thread().name)
    

list_of_threads = enumerate()
print("\nList of active threads now: ")
for thread in list_of_threads: 
    print(f"Thread Name: {thread.name}, Thread ID: {thread.ident}")
print("\n")


t = child()
print("Current thread is: ",current_thread().name)
print("Im starting child thread...")
t.start()

list_of_threads = enumerate()
print("\nList of active threads after creating child thread instance: Note: this code is executed by the thread: ",current_thread().name)
for thread in list_of_threads: 
    print(f"LIST OF THREADS STATEMENT: Thread Name: {thread.name}, Thread ID: {thread.ident}")
print("\n")

for _ in range(10):
    print("MAIN THREAD STATEMENT: I'm a parent thread: ",{current_thread().name})


print("here, u can see hwo chidl thread and parent thread statemtns overlap during printing, since they are executing simultaneosuly. First, the child thread statemtns are overlapping with the main thread's list of thread print statements during simultaenoues execution,then after list of threads task completion, it overlaps with the main thread's parent thread printing statement task, thus runnign simultaenously.To make sure, a thread waits till the completion of another thread,to avoid overlapping like this, we need to use.join() method. We'll use that method in the enxt e.g.,\n")

print("3) Using Class, without extending the Thread class: (OOPs Way)")

list_of_threads = enumerate()
print("\nList of active threads now: ")
for thread in list_of_threads: 
    print(f"LIST OF THREADS STATEMENT:Thread Name: {thread.name}, Thread ID: {thread.ident}")
print("\n")

class square:
    def sq(self,li):
        time.sleep(5)
        for i in li:
            print(f"Square of {i} is {i*i} by {current_thread().name}")
 
class multiply:
    def mul(self,li):
        time.sleep(5)
        for i in li:
            print(f"Multiplied by 2 of {i} is {i*2} by {current_thread().name}")

li = [1,2,3,4,5]
s = square()
m = multiply()
print("To give arguments to our thread object, as sq and mul function req., li to execute, we'll need another argument called args in the Thread object creation. ")
child_thread_1 = Thread(target = s.sq, name = "child_thread_1", args = (li,))
child_thread_2 = Thread(target = m.mul, name = "child_thread_2", args = (li,))


print("Setting/modifying the thread names using ref_var.name = '' or ref_var.setName(''): Thread-3 = Square, Thread-4: Multiply")
child_thread_1.name = "Square"
child_thread_2.name = "Multiply"

print("WE can find no of active threads using active_count, if i print this statement, after starting both child threads, it will print in between them. But i want it to print no of active count of threads immeddiately after starting child 1 and 2 at the start,after starign, not in between print statemetns. To achieve, that as we know, this print statemnt is beigne xecuted y the main thread, and not by the child threads, so afters starting the child threads,ill make them sleep,so that since both child threads are sleeoping,they won;t be able to print anything,so our main thread woudl print this staemten first")

print("Starting 2 child threads.....")
child_thread_1.start()
child_thread_2.start()
print("No of active threads = ",active_count(),"Executed by",current_thread().name)
print("Check whether a thread is alive or not using is_alive() method: ")
print("Do child-1 thread is alive now?",child_thread_1.is_alive())
print("Do child-2 thread is alive now?",child_thread_2.is_alive())
list_of_threads = enumerate()
for thread in list_of_threads: 
    print(f"LIST OF THREADS STATEMENT BEFORE JOIN: Thread Name: {thread.name}, Thread ID: {thread.ident}")
print("\n")
print("Now, I need to print this list of threads statement again, but only after complete exxecution of boht of the chidl threads, to know he active threads at last after execution completion of mul., and square., To do that, the main thread should wait till both child threads are completed. Then, only it should executes it's task. This will make sure LIST OF THREADS STATEMENT's will execute at last, after dispalyinf sqaure and multiplication, not in between overlapping displays like the previous eg.'s. To do that, we;ll use join(). It will make main thread to wait till both child threads complete")


child_thread_1.join()
child_thread_2.join()


list_of_threads = enumerate()
print("\nList of active threads now, after main thread waiting for child thread 1 and 2 to complete: ")
for thread in list_of_threads: 
    print(f"LIST OF THREADS STATEMENT ATLAST AFTER JOIN:Thread Name: {thread.name}, Thread ID: {thread.ident}")
print("Do child-1 thread is alive now?",child_thread_1.is_alive())
print("Do child-2 thread is alive now?",child_thread_2.is_alive())

print("\n")
print("U might think if we use join() for all the threads, to wait unitl compeltion of another thread, it becomes like  a sequential flow, then better go with single thread i.e noraml process execution, but even those cases, multi-threading may be ebneficail, let us see a e.g, case scenario of it")


def venue():
    print("Searching for best venue....")
    time.sleep(5)
    global venue
    venue = "Leela Palace"
    print("Ater long discussions venue is finalised as, ",venue)

def invitation_printing():
    global color
    global size
    global design
    global other_details
    print("Here, even though i can print the invitaions, only after finalising the venue, ther is no neeed to wait compeltetly till they decide the place. Let, me deciede teh color,shape,design and fill alld etaisl in teh invitaiton,leaving space ot venu, after venu gets decided,then ill print the invitations.THus, multi-threading is useful here. If i use signle-threading, I would be waiting till venu is finalsied, even fro decidiing teh design of the invitaiton")
    color = "Blue"
    size = "16x16"
    design = "Box-Shaped"
    other_details = "Bride Name: X, Groom Name: Y"
    final_venue.join()
    print(f"Invitation: \n {other_details} \n  Venue: {venue}")


def marriage_arrangements():
    print("here,unlike invitation waiting forever for venue finalsiation, to print, we'll not wait forever, for invitation to complete to marraige. We'll do all other works, and wait for a speciif amt., of time. If invitation not gets pritned even after comepteing otehr thigns and waiting for a certain amt fo time, directly marriage will be done.")

    print("Decorations work chosen...")
    print("List of relatives invitations needs to be sent gets decided.....")
    print("All other catering arranagements are beign planned....")
    print("All other marraige works completed, Ill wait till some more time. IF still i dint get invitaiton, marraige will be done straightly")
    invitation.join(10)
    print("Marriage completed successfully")


final_venue = Thread(target = venue)
invitation = Thread(target = invitation_printing)
marriage = Thread(target = marriage_arrangements)

final_venue.start()
invitation.start()
marriage.start()
print("here, eventhough the sequentail order is : Venue finalisation -> Invitaiton printing - > Marriage, since we used multi-threading instead of single threading, we completed all other independednt works of each tasks simultaneously, and each thread, waited only in their crucial dependedncy part, whcih depends on the prev ., sequentail order task for execution, making the overall process faster.")


marriage.join()
print("\n Daemon Threads: These are background running threads e.,g garbage collector, which gives support to non-daemon threads e.g, main thread. Example Scenario: Whenever the executing program (main thread) gets memory issues, garbage collector (daemon thread) gives support to free up the resources. By default, Main thread is a non-daemon thread. For all other threads, other than main thread are daemon/non-daemon by default, based on their parent nature. The child thread's daemon/non-daemon nature is inherited from the parent thread. It is possible to make any thread daemon/non-daemon using setDaemon(True/False) method. But, once a thread is started, is not not possible to change it's daemon nature. The biggest advantage of Daemon threads is, when the last non-daemon thread terminates, automatically, all the daemon threads will also terminate. We need not need to manually terminate it e.g, In a  car race game, allt eh surroundings such as Sceneries,streetlights, roads, obstacles needs to eb showsn only till the last car is present in the race. After tha last car (non-daemon/main thread) completes the race, there is no need to show all teh surrroundings,sceneries will automatically closes (daemon threads). SO,all teh main jobs need to be done by non-daemon threads, and supporting jobs needs to be done by daemon threads.")
t = current_thread()
print("Do the main thread is daemon?", t.isDaemon())
print("Do the main thread is daemon?", t.daemon)

try:
    t.setDaemon(True)
except Exception as e:
    print(f"Error is {e}. It is not possible to modify daemon nature of a thread, after it is started. So, only we can modify the daemon nature ofa ll other threads, but when it comes to Main thread, it's starting is not in out hand, it's already started. So, we cannot modify or make the main thread daemon")

time.sleep(5)

def obstacles():
    for _ in range(100):
        print("Obstacles are showing in the surroundings...")

def surroundings():
    for _ in range(100):
        print("Sceneries, roads, traffic signals are showing in the surroundings...")

def race(cars):
    for i in cars:
        print(f"{i}th Car completed the race out of the 5 cars")

s1 = Thread(target = race,args = ([1,2,3,4,5],))
s2 = Thread(target = obstacles)
s3 = Thread(target = surroundings)
s2.daemon = True
s3.daemon = True
print("Daemon Status of Race Cars is: ",s1.daemon)
print("Daemon Status of obstacles is: ",s2.daemon)
print("Daemon Status of surroundings is: ",s3.daemon)
print("you can observe,as soon as i start all these threads to execute in the car game, all the supporting function threads like obstacles adn usrrounding objects will be executed till the car is still present in teh race, after all cars finishes the race, all the supporitng functions will automatically terminates, before comeplteing their total execution iterations, since they are daemon threads, and they can exist only if a non-daemon exists. As last non-daemon thread i.e s1 terminates(5th car completes the race), supproting daemon threads will also terminate automatically.")
s1.start()
s2.start()
s3.start()











