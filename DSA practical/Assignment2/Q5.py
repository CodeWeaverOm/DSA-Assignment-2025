print("Om Nimmalwar")

queue = []

def enqueue():
    val = int(input("Enter value: "))
    pri = int(input("Enter priority (lower = higher priority): "))
    queue.append((val,pri))
    queue.sort(key= lambda x:x[1])   
    print(f"{val} Enqueued with priority {pri}")

def dequeue():
    if not queue:
        print("Queue Underflow")
    else:
        val,pri= queue.pop(0)
        print(f"Dequeued:{val} Priority:{pri}")

def display():
    if not queue:
        print("Queue Empty")
    else:
        print("Queue Elements(value,priority):")
        for item in queue:
            print(item)

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
