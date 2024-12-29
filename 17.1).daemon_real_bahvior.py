from threading import *
print("\nReal Daemon Behaviour:\n")
def child_thread_2():
    print("Im the running child thread 2",current_thread().name, "whose daemon status is",current_thread().daemon,"since my parent is thread s1, which is daemon in nature,i inherited that property")

def child_thread_1():
    print("Im the running child thread 1",current_thread().name, "whose daemon status is",s1.daemon)
    s2 = Thread(target=child_thread_2)
    print("S2 child thread's daemon status: ",s2.daemon)
    s2.start()
    
s1 = Thread(target = child_thread_1)
print("Do the child thread is daemon?", s1.daemon,"Since, it's daemon nature is inherited from it's parent thread(main thread)")
#s1.setDaemon(True)
s1.daemon = True
print("Do the child thread is daemon now?", s1.daemon)
print("Child thread s is started, herafter it's daemon nature cant'be altered.")
print("here, after i start s1(daemon thread) from main thread(non-deamon thread), since there is no further execution cmds availabe for main thread,main thread terminates immediately. As main thread termiantes immdeiatly, teh daemon thread s1 which is parallely executing, also terminates immedtiaely,so the child_thread_1 woudl not be executed compeltely, so the s2 deaomn thread starting inside the chidl_thread_1 also would not be executed, as it's parent s1 function itself stops execution immediately,after main thread termination.")
s1.start()
print("Main thread execution ends immediately here!")