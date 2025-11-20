print("Om Nimmalwar")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        n = Node(data)
        if self.rear is None:
            self.front = self.rear = n
        else:
            self.rear.next = n
            self.rear = n
        print(data, "Enqueued")

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
        else:
            print("Dequeued:", self.front.data)
            self.front = self.front.next
            if self.front is None:
                self.rear = None

    def display(self):
        if self.front is None:
            print("Queue Empty")
        else:
            temp = self.front
            print("Queue Elements:")
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()
q = Queue()

while True:
    ch = int(input("\n1. ENQUEUE  2. DEQUEUE  3. DISPLAY  4. EXIT \nEnter your choice: "))

    if ch == 1:   
        q.enqueue(int(input("Enter value: ")))
    elif ch == 2:
        q.dequeue()
    elif ch == 3:
        q.display()
    elif ch == 4:
        print("Exiting program:")
        break
    else:
        print("Invalid choice")
