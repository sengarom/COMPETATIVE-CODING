class Solution:
    def subsets(self, nums):
        result = []
        n = len(nums)
        total = 1 << n  # Total number of subsets is 2^n

        for mask in range(total):  # Generate every possible bitmask
            current = []

            for i in range(n):
                if mask & (1 << i):  # Check if the i-th bit is set
                    current.append(nums[i])  # Include the element

            result.append(current)  # Store the current subset

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