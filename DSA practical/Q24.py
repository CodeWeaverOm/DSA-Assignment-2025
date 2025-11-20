class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def delete_begin(head):
    if head is None:
        return None
    return head.next
