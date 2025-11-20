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

def minNode(t):
    while t.l: t = t.l
    return t

def delete(t, x):
    if not t: return t
    if x < t.x: t.l = delete(t.l, x)
    elif x > t.x: t.r = delete(t.r, x)
    else:
        if not t.l: return t.r
        if not t.r: return t.l
        m = minNode(t.r)
        t.x = m.x
        t.r = delete(t.r, m.x)
    return t

def inorder(t):
    if t:
        inorder(t.l)
        print(t.x, end=" ")
        inorder(t.r)


root = None
for n in [50, 30, 70, 20, 40]:
    root = insert(root, n)

print("Before delete:")
inorder(root)

root = delete(root, 30)

print("\nAfter delete:")
inorder(root)
