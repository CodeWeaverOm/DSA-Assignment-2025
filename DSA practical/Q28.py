class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.count = 0

    def insert(self, data):
        new = Node(data)
        self.count += 1
        if self.head is None:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new
        new.prev = temp
    def search_DLL(head, key):
        pos = 1
        temp = head
        while temp:
            if temp.data == key:
                return pos
            pos += 1
            temp = temp.next
        return -1

    def get_count(self):
        return self.count

dll = DLL()
dll.insert(10)
dll.insert(20)
dll.insert(30)
print("Count =", dll.get_count())
