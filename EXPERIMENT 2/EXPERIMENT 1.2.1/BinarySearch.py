arr = []
print("enter array size:")
n = int(input())
print("enter array elements:")
for i in range(n):
    arr.append(int(input()))

new = int(input("enter new element:"))

start = 0
end = n - 1
while start <= end:
    mid = (start + end) // 2
    if arr[mid] == new:
        print("element found at index:", mid)
        break
    elif arr[mid] < new:
        start = mid + 1
    else:
        end = mid - 1
        
print("inserting at index:", start)

    