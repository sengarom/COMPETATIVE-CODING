
class Solution:
    def coinChange(self, coins, amount):
        # amount + 1 acts as infinity
        dp = [amount + 1] * (amount + 1)

        # Zero amount requires zero coins
        dp[0] = 0

        # Calculate answer for every amount
        for a in range(1, amount + 1):
            # Try every coin
            for c in coins:
                if c <= a:
                    dp[a] = min(dp[a], dp[a - c] + 1)

        # If still infinity, amount is impossible
        if dp[amount] == amount + 1:
            return -1

        return dp[amount]


obj = Solution()

n = int(input("Enter number of coins: "))

coins = list(map(int, input("Enter coin denominations: ").split()))

amount = int(input("Enter amount: "))

print("Minimum coins:", obj.coinChange(coins, amount))
