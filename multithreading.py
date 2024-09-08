import threading

"""
Introduction:
Multithreading allows a CPU to execute multiple threads concurrently. 
This improves efficiency by performing multiple operations at the same time, 
making better use of CPU resources.
"""

# Example of creating and running threads:

def function1():
    """
    Function to print 'one' 10,000 times.
    """
    for x in range(10000):
        print("one")

def function2():
    """
    Function to print 'two' 10,000 times.
    """
    for x in range(10000):
        print("two")

# Create threads for function1 and function2
t1 = threading.Thread(target=function1)  
t2 = threading.Thread(target=function2)  

# Start the threads
t1.start()  
t2.start()  

# Wait for both threads to complete
t1.join()  
t2.join()  

def hello():
    """
    Function to print 'Hello!' 50 times.
    """
    for x in range(50):
        print("Hello!")

# Create and start a new thread for the hello function
t1 = threading.Thread(target=hello)  
t1.start()  

# Wait for the hello thread to complete before printing the final statement
t1.join()  

print("Another print statement text")  
