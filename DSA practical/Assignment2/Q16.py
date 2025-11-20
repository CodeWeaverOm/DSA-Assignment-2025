print("Om Nimmalwar")

# ------------------- LINKED LIST -------------------
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# ------------------- ADJACENCY LIST -------------------
class AdjList:
    def __init__(self, n):
        self.n = n
        self.heads = [None] * n     # storing head pointers only

    # add edge u -> v
    def add_edge(self, u, v):
        newNode = ListNode(v)
        newNode.next = self.heads[u]
        self.heads[u] = newNode


# ------------------- MANUAL QUEUE -------------------
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, val):
        newNode = ListNode(val)
        if self.rear is None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def dequeue(self):
        if self.front is None:
            return None
        value = self.front.val
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def empty(self):
        return self.front is None


# ------------------- DFS -------------------
def dfs(v, visited, graph):
    visited[v] = 1
    print(v, end=" ")

    temp = graph.heads[v]
    while temp is not None:
        if visited[temp.val] == 0:
            dfs(temp.val, visited, graph)
        temp = temp.next


# ------------------- BFS -------------------
def bfs(start, graph):
    visited = [0] * graph.n
    q = Queue()

    visited[start] = 1
    q.enqueue(start)

    while not q.empty():
        v = q.dequeue()
        print(v, end=" ")

        temp = graph.heads[v]
        while temp is not None:
            if visited[temp.val] == 0:
                visited[temp.val] = 1
                q.enqueue(temp.val)
            temp = temp.next


# ------------------- INPUT -------------------
n = int(input("Vertices: "))
graph = AdjList(n)

e = int(input("Edges: "))
print("Enter edges (u v):")
i = 0
while i < e:
    s = input().split()
    u = int(s[0])
    v = int(s[1])
    graph.add_edge(u, v)
    graph.add_edge(v, u)
    i += 1

start = int(input("Start vertex: "))

# ------------------- OUTPUT -------------------
print("DFS:", end=" ")
dfs(start, [0]*n, graph)
print()

print("BFS:", end=" ")
bfs(start, graph)
