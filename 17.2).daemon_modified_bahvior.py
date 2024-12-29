from threading import *

print("\nModified Daemon Behaviour\n")
def child_thread_2():
    print("Im the running child thread 2",current_thread().name, "whose daemon status is",current_thread().daemon,"since my parent is thread s1, which is daemon in nature,i inherited that property")

def child_thread_1():
    print("Im the running child thread 1",current_thread().name, "whose daemon status is",s1.daemon)
    s2 = Thread(target=child_thread_2)
    print("S2 child thread's daemon status: ",s2.daemon)
    print("S2 threas is starting...")
    s2.start()

s1 = Thread(target = child_thread_1)
print("Do the child thread is daemon?", s1.daemon,"Since, it's daemon nature is inherited from it's parent thread(main thread)")
#s1.setDaemon(True)
s1.daemon = True
print("Do the child thread is daemon now?", s1.daemon)
print("Child thread s is started, herafter it's daemon nature cant'be altered.")
print("Here, after i start s1(daemon thread) from main thread(non-deamon thread), i used s1.join() ensuring the non-demon main thread will never terminates, or continue its execution until, s1 complets its execution. IF s1 deaon thread executes succesfuly, it's chld daemon thread will also execute successfully wihtut any issues as it is implemented inside it, and after their successful execution, main thread will terminate.")
s1.start()
s1.join()
print("Main thread execution ends here!")

