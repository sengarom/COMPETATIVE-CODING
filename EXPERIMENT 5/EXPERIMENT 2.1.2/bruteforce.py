class Solution:
    def __init__(self):
        self.uniqueCombinations = set()

    def backtrack(self, candidates, remaining, current):
        # Target reached
        if remaining == 0:
            combination = tuple(sorted(current))
            # Set removes duplicate combinations
            self.uniqueCombinations.add(combination)
            return

        # Target exceeded
        if remaining < 0:
            return

        # Try every candidate
        for i in range(len(candidates)):
            current.append(candidates[i])  # Choose candidate

            self.backtrack(
                candidates,
                remaining - candidates[i],
                current
            )  # Explore

            current.pop()  # Backtrack

    def combinationSum(self, candidates, target):
        self.uniqueCombinations = set()
        current = []

        self.backtrack(candidates, target, current)

        # Convert set of tuples into a list of lists
        result = [list(combination)
                  for combination in sorted(self.uniqueCombinations)]

        return result


def main():
    n = int(input("Enter number of candidates: "))
    candidates = list(map(int, input("Enter candidates: ").split()))

    target = int(input("Enter target: "))

    obj = Solution()
    result = obj.combinationSum(candidates, target)

    print("Unique combinations:")
    for combination in result:
        print("[" + ",".join(map(str, combination)) + "]")


if __name__ == "__main__":
    main()