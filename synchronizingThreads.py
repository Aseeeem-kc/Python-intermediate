import threading
import time

"""
Introduction:
This script demonstrates the use of locking and semaphores in multithreading.
- **Locking**: Ensures that only one thread can access a critical section of code at a time.
- **Semaphores**: Control access to a resource by multiple threads, managing concurrent access.
"""

# Locking Example

x = 8192
lock = threading.Lock()

def double():
    """
    Doubles the global variable x until it reaches or exceeds 16,384.
    Uses a lock to prevent simultaneous access to the variable by multiple threads.
    """
    global x, lock
    lock.acquire() 
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)
    print("Reached the maximum!")
    lock.release()

def halve():
    """
    Halves the global variable x until it drops to 1 or below.
    Uses a lock to prevent simultaneous access to the variable by multiple threads.
    """
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("Reached the minimum!")
    lock.release()

# Create threads for halving and doubling
t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)

# Start threads
t1.start()
t2.start()

# Semaphores Example

semaphore = threading.BoundedSemaphore(value=5)

def access(thread_number):
    """
    Simulates access to a shared resource controlled by a semaphore.
    Each thread tries to acquire the semaphore, simulates access, and then releases it.
    """
    print("{} is trying to access".format(thread_number))
    semaphore.acquire()
    print("{} was granted access!".format(thread_number))
    time.sleep(5)
    print("{} is now releasing".format(thread_number))
    semaphore.release()
    print("{} released".format(thread_number))

# Create and start threads that attempt to access the resource
for thread_number in range(1, 11):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()
    time.sleep(1)
