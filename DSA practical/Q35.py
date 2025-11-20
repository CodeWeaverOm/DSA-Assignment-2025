class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def merge_DLL(h1, h2):
    dummy = Node(0)
    temp = dummy

    while h1 and h2:
        if h1.data < h2.data:
            temp.next = h1
            h1.prev = temp
            h1 = h1.next
        else:
            temp.next = h2
            h2.prev = temp
            h2 = h2.next
        temp = temp.next

    rem = h1 if h1 else h2

    while rem:
        temp.next = rem
        rem.prev = temp
        rem = rem.next
        temp = temp.next

    head = dummy.next
    if head:
        head.prev = None
    return head
