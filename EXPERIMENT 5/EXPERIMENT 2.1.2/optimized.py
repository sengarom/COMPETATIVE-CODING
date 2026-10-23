class Solution:
    def backtrack(self, candidates, start, current, remaining, result):
        # Target reached
        if remaining == 0:
            result.append(current.copy())
            return

        # Try candidates from the current index
        for i in range(start, len(candidates)):

            # Prune if candidate is larger than remaining target
            if candidates[i] > remaining:
                break

            current.append(candidates[i])  # Choose candidate

            # Use i again because repetition is allowed
            self.backtrack(
                candidates, i, current,
                remaining - candidates[i], result
            )

            current.pop()  # Backtrack

    def combinationSum(self, candidates, target):
        result = []
        current = []

        # Sort candidates for effective pruning
        candidates.sort()

        self.backtrack(candidates, 0, current, target, result)

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