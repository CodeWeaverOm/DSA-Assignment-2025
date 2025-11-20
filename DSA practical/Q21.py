class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_last(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

ll = LinkedList()
ll.insert_last(10)
ll.insert_last(20)
ll.insert_last(30)
ll.display()
