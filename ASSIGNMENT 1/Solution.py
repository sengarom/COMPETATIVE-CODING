#LEET CODE - 81. Search in Rotated Sorted Array II

def search(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return True

        if nums[low] == nums[mid]:
            low += 1
            continue

        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return False


n = int(input("Enter the number of elements: "))
nums = list(map(int, input("Enter the elements (space-separated): ").split()))
target = int(input("Enter the target element: "))

if len(nums) != n:
    print("Error: Number of elements entered does not match n.")
else:
    if search(nums, target):
        print("Target found")
    else:
        print("Target not found")