def contains_nearby_duplicate(nums, k):
    s = set()

    for i in range(len(nums)):
        if i > k:
            s.remove(nums[i - k - 1])

        if nums[i] in s:
            return True

        s.add(nums[i])

    return False


n = int(input())
nums = list(map(int, input().split()))
k = int(input())

print("true" if contains_nearby_duplicate(nums, k) else "false")