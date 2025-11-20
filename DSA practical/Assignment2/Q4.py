print("Om Nimmalwar")

MAX = 5

class Queue:
    def __init__(self):
        self.queue = [None] * MAX   # fixed-size array
        self.front = -1
        self.rear = -1

    def enqueue(self, val):
        if self.rear == MAX - 1:
            print("Queue Overflow")
        else:
            if self.front == -1:   # first element
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = val
            print(val, "Enqueued")

    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Empty")
        else:
            print("Dequeued:", self.queue[self.front])
            self.front += 1

    def display(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Empty")
        else:
            print("Queue Elements:", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


queue = Queue()

while True:
    print("\n1. ENQUEUE  2. DEQUEUE  3. DISPLAY  4. EXIT")
    ch = int(input("Enter choice: "))

    if ch == 1:
        val = int(input("Enter value: "))
        queue.enqueue(val)
    elif ch == 2:
        queue.dequeue()
    elif ch == 3:
        queue.display()
    elif ch == 4:
        print("Exiting program...")
        break
    else:
        print("Invalid choice")
