class Solution:
    def backtrack(self, nums, start, current, result):
        # Store the current subset
        result.append(current.copy())

        # Try every element from the current index
        for i in range(start, len(nums)):
            current.append(nums[i])  # Include the current element

            self.backtrack(nums, i + 1, current, result)  # Move to the next index

            current.pop()  # Backtrack and remove the last element

    def subsets(self, nums):
        result = []
        current = []

        self.backtrack(nums, 0, current, result)

        return result


def main():
    n = int(input("Enter number of elements: "))
    nums = list(map(int, input("Enter elements: ").split()))

    obj = Solution()
    result = obj.subsets(nums)

    print("All subsets:")
    for subset in result:
        print("[" + ",".join(map(str, subset)) + "]")


if __name__ == "__main__":
    main()