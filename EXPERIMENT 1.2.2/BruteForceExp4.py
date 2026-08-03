arr = []
print("enter array size:")
n = int(input())
print("enter array elements:")
for i in range(n):
    arr.append(int(input()))

new = int(input("enter element to search:"))
j = -1
for i in range(n):
    if arr[i] == new:
        j = i
        break

if j != -1:
    print("element found")
else:
    print(j)
               
