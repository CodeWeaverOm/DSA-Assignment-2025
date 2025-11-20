class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new
        new.prev = temp

    def sum_alternate(self):
        temp = self.head
        i = 1
        s = 0
        while temp:
            if i % 2 != 0:
                s += temp.data
            i += 1
            temp = temp.next
        return s

dll = DLL()
dll.insert_end(5)
dll.insert_end(10)
dll.insert_end(15)
dll.insert_end(20)
print(dll.sum_alternate())
