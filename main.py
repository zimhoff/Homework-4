import threading
import time

# Define semaphores
mutex = threading.Semaphore(1)
full = threading.Semaphore(0)
empty = threading.Semaphore(5)

# Define buffer
buffer = [0] * 5

# Define producer function
def producer():
    global buffer
    for i in range(1, 11):
        empty.acquire()
        mutex.acquire()
        buffer[i % 5] = i
        print("Produced", i)
        mutex.release()
        full.release()
        time.sleep(1)

# Define consumer function
def consumer():
    global buffer
    for i in range(1, 11):
        full.acquire()
        mutex.acquire()
        item = buffer[(i-1) % 5]
        buffer[(i-1) % 5] = 0
        print("Consumed", item)
        mutex.release()
        empty.release()
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

