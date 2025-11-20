class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_zero_sum(head):
    dummy = Node(0)
    dummy.next = head
    prefix_sum = 0
    sum_map = {}

    temp = dummy
    while temp:
        prefix_sum += temp.data

        if prefix_sum in sum_map:
            prev = sum_map[prefix_sum]
            start = prev.next
            s = prefix_sum
            while start != temp:
                s += start.data
                if s in sum_map:
                    del sum_map[s]
                start = start.next
            prev.next = temp.next
        else:
            sum_map[prefix_sum] = temp

        temp = temp.next

    return dummy.next
