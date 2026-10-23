
class Solution:
    def solve(self, coins, amount):
        # Zero amount needs zero coins
        if amount == 0:
            return 0

        best = float('inf')

        # Try every possible coin
        for c in coins:
            if c <= amount:
                result = self.solve(coins, amount - c)

                # Check if remaining amount is possible
                if result != float('inf'):
                    best = min(best, result + 1)

        return best

    def coinChange(self, coins, amount):
        result = self.solve(coins, amount)

        # Return -1 if amount cannot be formed
        if result == float('inf'):
            return -1

        return result


obj = Solution()

n = int(input("Enter number of coins: "))

coins = list(map(int, input("Enter coin denominations: ").split()))

amount = int(input("Enter amount: "))

print("Minimum coins:", obj.coinChange(coins, amount))
