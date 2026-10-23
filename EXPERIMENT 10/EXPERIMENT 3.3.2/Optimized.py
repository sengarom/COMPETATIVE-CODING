
class Solution:
    def dfs(self, grid, visited, r, c):
        m = len(grid)
        n = len(grid[0])

        # Check boundaries, water, and visited cells
        if (r < 0 or r >= m or c < 0 or c >= n
                or grid[r][c] == '0' or visited[r][c]):
            return

        # Mark current cell visited
        visited[r][c] = True

        # Visit four directions
        self.dfs(grid, visited, r - 1, c)
        self.dfs(grid, visited, r + 1, c)
        self.dfs(grid, visited, r, c - 1)
        self.dfs(grid, visited, r, c + 1)

    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        count = 0

        visited = [[False] * n for _ in range(m)]

        # Scan every cell
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and not visited[r][c]:
                    # Found a new island
                    count += 1
                    self.dfs(grid, visited, r, c)

        return count


obj = Solution()

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

grid = []
print("Enter grid:")
for i in range(m):
    row = list(input().split())
    grid.append(row)

print("Number of Islands:", obj.numIslands(grid))
