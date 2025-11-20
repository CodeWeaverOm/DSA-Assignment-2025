print("Om Nimmalwar")

MAX = 100

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
            return None
        ch = self.stack[self.top]
        self.top -= 1
        return ch

    def is_empty(self):
        return self.top == -1


def is_balanced(expr):
    st = Stack()
    for ch in expr:
        if ch in "([{":
            st.push(ch)
        elif ch in ")]}":
            top = st.pop()
            if top is None:
                return False
            if (ch == ')' and top != '(') or \
               (ch == ']' and top != '[') or \
               (ch == '}' and top != '{'):
                return False
    return st.is_empty()


expr = input("Enter expression: ")
if is_balanced(expr):
    print("Parentheses are Balanced")
else:
    print("Parentheses are Not Balanced")
