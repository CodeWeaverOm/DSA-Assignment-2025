print("Om Nimmalwar")

# ---------------- LINKED LIST FOR ADJACENCY ----------------
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


# ---------------- MANUAL DICTIONARY ----------------
class KVNode:
    def __init__(self, key, head):
        self.key = key
        self.head = head
        self.next = None


class ManualDict:
    def __init__(self):
        self.start = None

    # Check if key exists without 'in'
    def find(self, key):
        temp = self.start
        while temp is not None:
            if temp.key == key:
                return temp
            temp = temp.next
        return None

    # Insert key if not exists
    def insert_key(self, key):
        node = self.find(key)
        if node is None:
            new_node = KVNode(key, None)
            new_node.next = self.start
            self.start = new_node
            return new_node
        return node


# ---------------- GRAPH CLASS ----------------
class Graph:
    def __init__(self):
        self.adj = ManualDict()

    def add_edge(self, u, v):
        # ensure u exists in dictionary
        entry = self.adj.insert_key(u)

        # add v to linked list of u
        newNode = ListNode(v)
        newNode.next = entry.head
        entry.head = newNode

    def display(self):
        temp = self.adj.start
        while temp is not None:
            print(temp.key, "->", end=" ")

            p = temp.head
            while p is not None:
                print(p.value, end=" ")
                p = p.next

            print()
            temp = temp.next


# ---------------- EXAMPLE ----------------
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

g.display()
