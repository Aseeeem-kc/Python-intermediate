import threading
import time

# Daemon Threads and Events in Threading

# **Daemon Threads**:
# - A daemon thread is a thread that runs in the background and does not prevent the program from exiting.
# - When the main program exits, daemon threads are abruptly stopped.
# - Useful for background tasks that should not block program termination.

# **Events**:
# - An Event is a synchronization primitive that allows threads to communicate with each other.
# - A thread can wait for an event to be set, and other threads can trigger the event by setting it.
# - Useful for coordinating tasks between threads.

# Example 1: Using Events
event = threading.Event()

def myFunction():
    """
    Function that waits for an event to be triggered before performing an action.
    """
    print("Waiting for event to trigger...")
    event.wait()  # Wait until the event is set
    print("Performing action XYZ now...")

# Create and start a thread that will wait for the event
t1 = threading.Thread(target=myFunction)
t1.start()

x = input("Do you want to trigger the event? (y/n)")

if x == "y":
    event.set()  # Trigger the event, allowing the waiting thread to proceed

# Example 2: Daemon Threads
path = "text.txt"
text = ""

def readFile():
    """
    Continuously reads the contents of a file and updates the global `text` variable.
    """
    global path, text
    while True:
        with open(path, "r") as f:
            text = f.read()
        time.sleep(3)  # Wait for 3 seconds before reading the file again

def printloop():
    """
    Continuously prints the current value of the `text` variable.
    """
    for x in range(30):
        print(text)
        time.sleep(1)  # Wait for 1 second before printing again

# Create and start a daemon thread for reading the file
t1 = threading.Thread(target=readFile, daemon=True)
t1.start()

# Create and start a non-daemon thread for printing the text
t2 = threading.Thread(target=printloop)
t2.start()
