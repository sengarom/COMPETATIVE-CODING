
from collections import deque


def validPath(n, edges, source, destination):
    # Build adjacency list for nodes 1 to n
    adj = [[] for _ in range(n + 1)]

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Source and destination are the same
    if source == destination:
        return True

    visited = [False] * (n + 1)
    q = deque()

    # Start BFS
    q.append(source)
    visited[source] = True

    while q:
        node = q.popleft()

        # Visit neighbours
        for next_node in adj[node]:
            if next_node == destination:
                return True

            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)

    return False


n = int(input("Enter number of nodes: "))
m = int(input("Enter number of edges: "))

edges = []
print("Enter edges:")
for i in range(m):
    u, v = map(int, input().split())
    edges.append([u, v])

source = int(input("Enter source: "))
destination = int(input("Enter destination: "))

print("Path Exists:", str(validPath(n, edges, source, destination)).lower())
