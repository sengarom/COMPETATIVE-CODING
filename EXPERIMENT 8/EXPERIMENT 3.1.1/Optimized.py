
class Solution:
    def climbStairs(self, n):
        # Base cases
        if n <= 2:
            return n

        prev1 = 1
        prev2 = 2

        # Calculate ways from step 3 to n
        for i in range(3, n + 1):
            current = prev1 + prev2

            # Shift the previous values
            prev1 = prev2
            prev2 = current

        return prev2


obj = Solution()
n = int(input("Enter number of stairs: "))
print("Number of ways:", obj.climbStairs(n))
