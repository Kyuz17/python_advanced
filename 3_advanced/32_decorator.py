# ADVANCED ***************************************************************************
# content = assignment
#
# date    = 2022-08-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************


"""
0. CONNECT the decorator "print_process" with all sleeping functions.
   Print START and END before and after.

   START *******
   main_function
   END *********


1. Print the processing time of all sleeping functions.
END - 00:00:00


2. PRINT the name of the sleeping function in the decorator.
   How can you get the information inside it?

START - long_sleeping

"""


import time


#*********************************************************************
# DECORATOR
def print_process(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"starting {func.__name__}")
        func(args)
        print(f"{func.__name__}" + " took " + f"{time.time() - start_time}")
    return wrapper


#*********************************************************************
# FUNC
@print_process
def short_sleeping(name):
    time.sleep(.1)
    print(name)

@print_process
def mid_sleeping(name):
    time.sleep(2)
    print(name)

@print_process
def long_sleeping(name):
    time.sleep(4)
    print(name)

short_sleeping("so sleepy")
long_sleeping("i slept enought")