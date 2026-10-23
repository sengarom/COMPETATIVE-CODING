
class Solution:
    def dfs(self, node, destination, adj, visited):
        # Destination reached
        if node == destination:
            return True

        # Mark current node visited
        visited[node] = True

        # Visit all connected nodes
        for next_node in adj[node]:
            if not visited[next_node] and self.dfs(
                next_node, destination, adj, visited
            ):
                return True

        return False

    def validPath(self, n, edges, source, destination):
        # Build adjacency list
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n

        return self.dfs(source, destination, adj, visited)


obj = Solution()

n = int(input("Enter number of nodes: "))
m = int(input("Enter number of edges: "))

edges = []
print("Enter edges:")
for i in range(m):
    u, v = map(int, input().split())
    edges.append([u, v])

source = int(input("Enter source: "))
destination = int(input("Enter destination: "))

print(str(obj.validPath(n, edges, source, destination)).lower())
