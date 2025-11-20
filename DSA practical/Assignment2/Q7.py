print("Om Nimmalwar")

MAX = 100  # maximum string length

class Stack:
    def __init__(self):
        self.stack = [None] * MAX
        self.top = -1

    def push(self, ch):
        if self.top == MAX - 1:
            print("Stack Overflow")
        else:
            self.top += 1
            self.stack[self.top] = ch

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return None
        else:
            ch = self.stack[self.top]
            self.top -= 1
            return ch

def reverse_string(s):
    st = Stack()
    # push all characters
    for ch in s:
        st.push(ch)

    rev = ''
    # pop until empty
    while st.top != -1:
        rev += st.pop()
    return rev

string = input("Enter a string: ")
print("Reversed String:", reverse_string(string))
