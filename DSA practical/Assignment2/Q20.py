print("Om Nimmalwar")
V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

indeg = [0]*V
outdeg = [0]*V

print("Enter edges (u v):")
for _ in range(E):
    u, v = map(int, input().split())
    outdeg[u] += 1
    indeg[v] += 1

print("\nVertex | In-degree | Out-degree")
for i in range(V):
    print(i, "      ", indeg[i], "        ", outdeg[i])
