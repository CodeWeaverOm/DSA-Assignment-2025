print("Om Nimmalwar")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        print(data, "pushed")

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            print(f"Popped:{self.top.data}")
            self.top = self.top.next

    def display(self):
        if self.top is None:
            print("Stack Empty")
        else:
            temp = self.top
            print("Stack elements:")
            while temp:
                print(temp.data)
                temp = temp.next

s = Stack()

while True:
    ch = int(input("\n1. PUSH  2. POP  3. DISPLAY  4. EXIT \nEnter your choice: "))

    if ch == 1:
        s.push( int(input("Enter value: ")))
    elif ch == 2:
        s.pop()
    elif ch == 3:
        s.display()
    elif ch == 4:
        print("Exiting program...")
        break
    else:
        print("Invalid choice")
