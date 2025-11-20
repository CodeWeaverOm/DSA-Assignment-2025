print("Om Nimmalwar")
import threading
import time


def print_square(n):
    sq = n * n
    print(f"Square of {n} = {sq}")


def print_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"Factorial of {n} = {fact}")



n = int(input("Enter a number: "))

start = time.time()  

t1 = threading.Thread(target=print_square, args=(n,))
t2 = threading.Thread(target=print_factorial, args=(n,))


t1.start()
t2.start()


t1.join()
t2.join()

end = time.time()    

print("\nTotal time taken =", end - start, "seconds")
