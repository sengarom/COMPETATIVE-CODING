
class Solution:
    def solve(self, i, height, k):
        # Base case: already at the first stone
        if i == 0:
            return 0

        best = float('inf')

        # Try all valid previous stones
        for j in range(max(0, i - k), i):
            cost = self.solve(j, height, k) + abs(height[i] - height[j])
            best = min(best, cost)

        return best

    def minCost(self, height, k):
        n = len(height)
        return self.solve(n - 1, height, k)


obj = Solution()

n = int(input("Enter number of stones: "))

height = list(map(int, input("Enter stone heights: ").split()))

k = int(input("Enter maximum jump distance k: "))

print("Minimum Cost:", obj.minCost(height, k))
