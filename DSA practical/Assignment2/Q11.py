print("Om Nimmalwar")
class Node:
    def __init__(self, x):
        self.x = x
        self.l = self.r = None

def insert(t, x):
    if not t: return Node(x)
    if x < t.x: t.l = insert(t.l, x)
    else: t.r = insert(t.r, x)
    return t

def inorder(t):
    if t:
        inorder(t.l)
        print(t.x, end=" ")
        inorder(t.r)

def preorder(t):
    if t:
        print(t.x, end=" ")
        preorder(t.l)
        preorder(t.r)

def postorder(t):
    if t:
        postorder(t.l)
        postorder(t.r)
        print(t.x, end=" ")

# Example
root = None
for n in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, n)

print("Inorder: ")
inorder(root)

print("\nPreorder: ")
preorder(root)

print("\nPostorder: ")
postorder(root)
