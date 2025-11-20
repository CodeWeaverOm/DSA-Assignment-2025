print("Om Nimmalwar")

MAX = 5
queue = [None] * MAX
front = -1
rear = -1

def enqueue():
    global front, rear
    if (rear + 1) % MAX == front:
        print("Queue Overflow ")
    else:
        val = int(input("Enter value: "))
        if front == -1: 
            front = rear = 0
        else:
            rear = (rear + 1) % MAX
        queue[rear] = val
        print(val, "Enqueued")

def dequeue():
    global front, rear
    if front == -1:
        print("Queue Underflow")
    else:
        print("Dequeued:", queue[front])
        if front == rear: 
            front = rear = -1
        else:
            front = (front + 1) % MAX

def display():
    global front, rear
    if front == -1:
        print("Queue Empty")
    else:
        print("Queue Elements:")
        i = front
        while True:
            print(queue[i])
            if i == rear:
                break
            i = (i + 1) % MAX

while True:
    print("\n1. ENQUEUE  2. DEQUEUE  3. DISPLAY  4. EXIT")
    ch = int(input("Enter choice: "))

    if ch == 1:
        enqueue()
    elif ch == 2:
        dequeue()
    elif ch == 3:
        display()
    elif ch == 4:
        print("Exiting program...")
        break
    else:
        print("Invalid choice")
