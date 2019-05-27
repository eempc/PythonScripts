import time

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

start_time = time.time()
factorial_1(10000)
end_time = time.time()
print("Factorial_1", round(end_time - start_time, 3))

# This is bad sleep as it locks everything
#time.sleep(5)

# This is good sleep as it allows CTRL-C every second
for i in range(5):
    time.sleep(1)



