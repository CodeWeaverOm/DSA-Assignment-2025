print("Om Nimmalwar")
class Node:
    def __init__(self, x):
        self.x = x
        self.l = self.r = None

def height(t):
    if t is None:
        return 0
    return 1 + max(height(t.l), height(t.r))

# Example tree
root = Node(10)
root.l = Node(20)
root.r = Node(30)
root.l.l = Node(40)
root.l.r = Node(50)

print("Height of tree =", height(root))
