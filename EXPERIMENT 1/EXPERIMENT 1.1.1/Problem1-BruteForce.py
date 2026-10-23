def containsNearbyDuplicate(nums, k):
    num_map = {}

    for i, num in enumerate(nums):
        if num in num_map and abs(i - num_map[num]) <= k:
            return True
        num_map[num] = i

    return False


# Main function
n = int(input("Enter number of elements: "))

nums = list(map(int, input("Enter the elements: ").split()))

k = int(input("Enter k: "))

print(containsNearbyDuplicate(nums, k))