arr = []
print("enter array size:")
n = int(input())
print("enter array elements:")
for i in range(n):
    arr.append(int(input()))

new = int(input("enter new element:"))

for i in range(n):
    if arr[i] == new:
        print("element found at index:", i)
        break

    elif new>arr[i]:
        j = i + 1
        
print("element not found, inserting at index:", j)        
