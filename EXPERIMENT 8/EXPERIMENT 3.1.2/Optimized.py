
class Solution:
    def minCost(self, height, k):
        n = len(height)

        # dp[i] stores minimum cost to reach stone i
        dp = [float('inf')] * n
        dp[0] = 0

        # Calculate minimum cost for each stone
        for i in range(1, n):
            # Check all reachable previous stones
            for j in range(max(0, i - k), i):
                cost = dp[j] + abs(height[i] - height[j])
                dp[i] = min(dp[i], cost)

        return dp[n - 1]


obj = Solution()

n = int(input("Enter number of stones: "))

height = list(map(int, input("Enter stone heights: ").split()))

k = int(input("Enter maximum jump distance k: "))

print("Minimum Cost:", obj.minCost(height, k))
