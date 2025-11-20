print("Om Nimmalwar")
MAX = 5

class Stack:
    def __init__(self):
        self.stack = [None] * MAX
        self.top = -1

    def push(self, value):
        if self.top == MAX - 1:
            print("Stack Overflow! (Stack is full)")
        else:
            self.top += 1
            self.stack[self.top] = value
            print(f"{value} pushed into stack")

    def pop(self):
        if self.top == -1:
            print("Stack Underflow! (Stack is empty)")
        else:
            value = self.stack[self.top]
            self.stack[self.top] = None 
            self.top -= 1
            print(f"Popped element: {value}")

    def display(self):
        if self.top == -1:
            print("Stack is empty!!")
        else:
            print("Stack elements (top to bottom):")
            for i in range(self.top, -1, -1):
                print(self.stack[i])


stack = Stack()

while True:
    print("\n1. PUSH  2. POP  3. DISPLAY  4. EXIT")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to push: "))
        stack.push(value)
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        stack.display()
    elif choice == 4:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again")
