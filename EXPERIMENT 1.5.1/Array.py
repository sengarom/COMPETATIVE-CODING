n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

odd = []
even = []

for i in range(n):
    if i % 2 == 0:
        odd.append(arr[i])
    else:
        even.append(arr[i])

result = odd + even

print("Result:", result)