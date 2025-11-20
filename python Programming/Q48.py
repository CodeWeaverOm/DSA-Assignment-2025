print("Om Nimmalwar")
import threading


lock = threading.RLock()


def factorial(n, name):
    lock.acquire()
    try:
        result = 1
        for i in range(1, n + 1):
            result *= i
        print(f"Factorial of {n} calculated by {name} = {result}")
    finally:
        lock.release()


def thread_task(num, name):
    factorial(num, name)


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))


t1 = threading.Thread(target=thread_task, args=(n1, "Thread-1"))
t2 = threading.Thread(target=thread_task, args=(n2, "Thread-2"))


t1.start()
t2.start()


t1.join()
t2.join()

print("Both factorials calculated successfully!")
