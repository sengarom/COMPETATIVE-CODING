arr = []

print("Enter array size:")
n = int(input())

print("Enter array elements (in sorted order):")
for i in range(n):
    arr.append(int(input()))

new = int(input("Enter element to search: "))

low = 0
high = n - 1
index = -1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == new:
        index = mid
        break
    elif arr[mid] < new:
        low = mid + 1
    else:
        high = mid - 1

if index != -1:
    print("Element found at index", index)
else:
    print(index)