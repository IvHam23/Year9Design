'''
mytimer.py - a program to test the speed of your computer
ilee - origina; coding, sept. 21, 2018
'''

# import timeit module
# only import the function required - speed up your code
from timeit import default_timer as timer

# defining a function called mytimer
def mytimer():
    
    start = timer()
    print(start)
    
    for i in range(1000000):  
        print(i)
        
    end = timer()
    print(end)
    
    print (end - start)
    
# calling or invoking the function mytimer
mytimer()