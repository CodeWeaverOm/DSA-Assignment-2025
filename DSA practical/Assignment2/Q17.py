print("Om Nimmalwar")

# ----------------------------------------
# Manually create an n x n matrix of zeros
# ----------------------------------------
n = int(input("Enter number of vertices: "))

graph = []
i = 0
while i < n:
    row = []
    j = 0
    while j < n:
        row += [0]     # manually adding element
        j += 1
    graph += [row]
    i += 1

# ----------------------------------------
# Take edges input manually (no map)
# ----------------------------------------
e = int(input("Enter number of edges: "))
print("Enter edges (u v):")

k = 0
while k < e:
    s = input().split()     # splitting text only
    u = int(s[0])
    v = int(s[1])
    graph[u][v] = 1
    graph[v][u] = 1
    k += 1

# ----------------------------------------
# Print adjacency matrix manually
# ----------------------------------------
print("Adjacency Matrix:")

i = 0
while i < n:
    j = 0
    while j < n:
        print(graph[i][j], end=" ")
        j += 1
    print()
    i += 1
