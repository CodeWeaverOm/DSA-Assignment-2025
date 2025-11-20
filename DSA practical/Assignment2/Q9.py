MAX = 100

class Stack:
    def __init__(self):
        self.stack = [None] * MAX
        self.top = -1

    def push(self, val):
        if self.top == MAX - 1:
            print("Stack Overflow")
        else:
            self.top += 1
            self.stack[self.top] = val

    def pop(self):
        if self.top == -1:
            return None
        val = self.stack[self.top]
        self.top -= 1
        return val

    def peek(self):
        if self.top == -1:
            return None
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1


def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

def is_right_associative(op):
    return op == '^'

def infix_to_postfix(expression):
    st = Stack()
    output = ""

    for char in expression:
        if char.isalnum():
            output += char
        elif char == '(':
            st.push(char)
        elif char == ')':
            while not st.is_empty() and st.peek() != '(':
                output += st.pop()
            st.pop()
        else:
            while (not st.is_empty() and st.peek() != '(' and
                   (precedence(st.peek()) > precedence(char) or
                   (precedence(st.peek()) == precedence(char) and not is_right_associative(char)))):
                output += st.pop()
            st.push(char)

    while not st.is_empty():
        output += st.pop()

    return output


expr = "A*(B+C)/D^E^F"
print("Infix:", expr)
print("Postfix:", infix_to_postfix(expr))
