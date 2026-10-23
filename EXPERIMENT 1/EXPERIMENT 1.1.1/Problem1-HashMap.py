def contains_nearby_duplicate(nums, k):
    m = {}  # Store last index of each number

    for i in range(len(nums)):
        n = nums[i]

        # Check if duplicate is within k distance
        if n in m and abs(i - m[n]) <= k:
            return True

        m[n] = i  # Update latest index

    return False


size = int(input())  # Read array size
nums = list(map(int, input().split()))  # Read array
k = int(input())  # Read allowed distance

# Print result
print("true" if contains_nearby_duplicate(nums, k) else "false")