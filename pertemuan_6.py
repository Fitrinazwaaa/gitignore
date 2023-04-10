# importing libraries
import time
import math

# decoration to calculate duration
# taken by nay function.
def calculate_time(func):


    # added arguments inside the inner1,
    # if function takesbany arguments,
    # can be added like this.
    def inner1(*args, **kwargs):

        # storing time before function execution....
        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution....
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1



# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):

    # slees 2 seconds because it takes very....
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))

# calling the function.
factorial(10)












