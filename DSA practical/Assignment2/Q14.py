print("Om Nimmalwar")

class Node:
    def __init__(self, x):
        self.x = x
        self.l = None
        self.r = None


# Check operator WITHOUT using "in"
def isOperator(c):
    return (c == '+') or (c == '-') or (c == '*') or (c == '/') or (c == '^')


# ------------ MANUAL STACK (NO BUILT-IN FUNCTIONS) ------------
class Stack:
    def __init__(self):
        self.data = []
        self.top = -1
    
    def push(self, value):
        self.top += 1
        # expand list manually
        if self.top == len(self.data):
            self.data = self.data + [value]
        else:
            self.data[self.top] = value
    
    def pop(self):
        if self.top == -1:
            return None
        value = self.data[self.top]
        self.top -= 1
        return value
    
    def peek(self):
        if self.top == -1:
            return None
        return self.data[self.top]


# ------------ CREATE EXPRESSION TREE ------------
def createExprTree(postfix):
    st = Stack()
    i = 0

    while i < len(postfix):
        ch = postfix[i]

        if isOperator(ch) == False:
            st.push(Node(ch))
        else:
            t = Node(ch)
            right = st.pop()
            left = st.pop()
            t.r = right
            t.l = left
            st.push(t)

        i += 1

    return st.peek()


# ------------ INORDER TRAVERSAL ------------
def inorder(t):
    if t is not None:
        inorder(t.l)
        print(t.x, end=" ")
        inorder(t.r)


# Example
postfix = "AB+C*"
root = createExprTree(postfix)

print("Inorder Traversal of Expression Tree:")
inorder(root)
