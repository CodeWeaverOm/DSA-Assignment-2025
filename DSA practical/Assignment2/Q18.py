
print("Om Nimmalwar")

# ------------------- BST NODE -------------------
class Node:
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None


# ------------------- INSERT -------------------
def insert(root, v):
    if root is None:
        return Node(v)
    if v < root.v:
        root.l = insert(root.l, v)
    else:
        root.r = insert(root.r, v)
    return root


# ------------------- MANUAL ARRAY APPEND -------------------
def arr_append(a, value):
    n = 0
    while n < len(a):
        n += 1

    # expand list manually
    a += [None]      # increase size
    a[n] = value     # store at last position


# ------------------- INORDER TRAVERSAL -------------------
def inorder(root, a):
    if root is not None:
        inorder(root.l, a)
        arr_append(a, root.v)
        inorder(root.r, a)


# ------------------- INPUT OF NUMBERS (NO map()) -------------------
nums = input("Enter nodes: ").split()

root = None

i = 0
while i < len(nums):
    val = 0
    s = nums[i]
    j = 0
    while j < len(s):           # manual string to integer
        val = val * 10 + (ord(s[j]) - 48)
        j += 1
    root = insert(root, val)
    i += 1


# ------------------- INPUT K -------------------
s = input("Enter K: ")
k = 0
i = 0
while i < len(s):
    k = k * 10 + (ord(s[i]) - 48)    # manual int
    i += 1


# ------------------- BUILD SORTED ARRAY -------------------
a = []
inorder(root, a)


# ------------------- FIND KTH SMALLEST -------------------
count = 0
i = 0
kth_smallest = None
while i < len(a):
    if count == k - 1:
        kth_smallest = a[i]
        break
    count += 1
    i += 1


# ------------------- FIND KTH LARGEST -------------------
count = 0
i = len(a) - 1
kth_large = None
while i >= 0:
    if count == k - 1:
        kth_large = a[i]
        break
    count += 1
    i -= 1


print("Kth Smallest:", kth_smallest)
print("Kth Largest:", kth_large)
