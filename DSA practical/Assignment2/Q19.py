print("Om Nimmalwar")

# --------------------- LINKED LIST NODE ---------------------
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# --------------------- ADJACENCY LIST ----------------------
class Graph:
    def __init__(self, V):
        self.V = V
        self.head = [None] * V   # only list used: fixed size pointer array

    def add_edge(self, u, v):
        # add v to u
        node1 = ListNode(v)
        node1.next = self.head[u]
        self.head[u] = node1

        # add u to v
        node2 = ListNode(u)
        node2.next = self.head[v]
        self.head[v] = node2


# --------------------- DFS CYCLE DETECTION ------------------
def dfs(v, parent, visited, graph):
    visited[v] = 1

    temp = graph.head[v]
    while temp is not None:
        x = temp.val
        if visited[x] == 0:             # not visited
            if dfs(x, v, visited, graph):
                return True
        elif x != parent:               # visited & not parent → cycle
            return True

        temp = temp.next

    return False


# ------------------------ INPUT -----------------------------
V = int(input("Vertices: "))
E = int(input("Edges: "))

graph = Graph(V)

print("Enter edges:")

i = 0
while i < E:
    edge = input().split()

    # manual conversion to int (no map)
    u_str = edge[0]
    v_str = edge[1]

    u = 0
    j = 0
    while j < len(u_str):
        u = u * 10 + (ord(u_str[j]) - 48)
        j += 1

    v = 0
    j = 0
    while j < len(v_str):
        v = v * 10 + (ord(v_str[j]) - 48)
        j += 1

    graph.add_edge(u, v)
    i += 1


# ------------------------ VISITED ARRAY ---------------------
visited = []
i = 0
while i < V:
    visited += [0]
    i += 1


# ------------------------ START DFS -------------------------
cycle = False
i = 0
while i < V:
    if visited[i] == 0:
        if dfs(i, -1, visited, graph):
            cycle = True
            break
    i += 1

# ------------------------ OUTPUT -----------------------------
if cycle:
    print("Cycle Exists")
else:
    print("No Cycle")
