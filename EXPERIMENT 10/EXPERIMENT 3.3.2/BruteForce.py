
class Solution:
    def dfs(self, grid, r, c):
        m = len(grid)
        n = len(grid[0])

        # Check boundaries and water
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
            return

        # Mark land as visited
        grid[r][c] = '0'

        # Visit four directions
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)

    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        count = 0

        # Scan every cell
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    # Found a new island
                    count += 1

                    # Sink the complete island
                    self.dfs(grid, r, c)

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
