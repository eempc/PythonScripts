import time
import threading


def factorial_1(x):
    result = 1
    for i in range(1,x):
        result *= i
    return result

def factorial_2(x):
    if x == 1:
        return x
    else:
        return x * factorial_2(x-1)

on_off = True

def do_something_every_seconds():
    i = 0

    while on_off:
        i += 1
        print("Thread 0:", i)
        time.sleep(0.25)



thread_0 = threading.Thread(target=do_something_every_seconds)
thread_0.start()

start_time = time.time()
factorial_1(10000)
end_time = time.time()
print("Factorial on main thread", round(end_time - start_time, 3))

def wait_a_bit(seconds):
    global on_off
    time.sleep(seconds)
    on_off = False
    print("Switched bool")

thread_1 = threading.Thread(target=wait_a_bit, args=[3])
thread_1.start()


# This is bad sleep as it locks everything
#time.sleep(5)

# This is good sleep as it allows CTRL-C every second (single thread)
#for i in range(5):
#    time.sleep(1)




