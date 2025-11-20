print("Om Nimmalwar")
class Node:
    def __init__(self, x):
        self.x = x
        self.l = self.r = None

def count_nodes(t):
    if t is None:
        return 0
    return 1 + count_nodes(t.l) + count_nodes(t.r)

# Example tree
root = Node(10)
root.l = Node(20)
root.r = Node(30)
root.l.l = Node(40)
root.l.r = Node(50)

print("Total nodes =", count_nodes(root))
