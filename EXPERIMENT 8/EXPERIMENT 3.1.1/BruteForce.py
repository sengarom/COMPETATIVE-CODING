
class Solution:
    def climbStairs(self, n):
        # Base cases
        if n <= 2:
            return n

        # Count ways from the previous two steps
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


n = int(input("Enter number of stairs: "))
obj = Solution()
print("Number of ways:", obj.climbStairs(n))
