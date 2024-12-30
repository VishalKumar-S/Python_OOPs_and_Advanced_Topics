import time
import random
print("Generators are used to return a sequence of values as output. It uses 'yield' keyword for it. It does not store the values in their memory, so memory issues can be avoided. It cang erneate one valeu at a time. So,whehever u need to have a sequence of values, and need only one at a time, use generators. Advantages of generators:\n 1. Better Performance.\n2. Better memory utilisation.\n3. When compared with normal iterators, generators are easy to use.\n4. Generators are best suitable for web scraping,wherever large amt of data is involved.")


def generator():
    yield '1st month groceries buy at Jan'
    yield '2nd month groceries buy at Feb'
    yield '3rd month groceries buy at Mar'


g = generator()
print("The type of g is: ",type(g))
print(next(g))
print(next(g))
print(next(g))
try:
    print(next(g))
except Exception as e:
    print("The error is",e,"There is no further elemetns to yield.SO,it throws error.")
try:
    MAX_SIZE = 10**(10000) 
    if MAX_SIZE > 10**5: 
        raise MemoryError("Attempting to allocate too much memory!")
    li = [x**x for x in range(MAX_SIZE)]
    print(li)


except Exception as e:
    print("It leads to memoery error, instead if we have used generator, we would'nt have faced this issue,as it wont store the value")
    def generate_values(n):
        i = 0
        while i<=n:
            yield i*i
            i+=1
    
    MAX_SIZE = 10**(1000000)
    for i in generate_values(MAX_SIZE):
        if i>10000:
            print("If i didnt break,it will execute forever. Our generator cacluated teh values on the fly,without storing all of them. So,always use generators instead of [i for i in range(10**100000)]")
            break
        print(i)


print("We can also use generators, like tuple comprehension format, here we need not give yield keyword expleicitely. It takes care of it internally.")
generator = (x**x for x in range(1000000000000))
count = 0
limit = 100


while(count<limit):
    print(next(generator))
    count+=1


print("Countdown eg.,: Here, in the below e.g., as value calls countdown(5),it doesnt perfrom the complete execution, instead it returns the countdown generator object, and that generator object is used in the for loop for iteration.")
def countdown(start):
    while start >= 0:
        yield start
        start -= 1

value = countdown(5)
print("Type of value is, ",value)
for number in value: 
    print("Countdown: ",number)



