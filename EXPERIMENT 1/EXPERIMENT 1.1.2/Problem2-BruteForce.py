def product_except_self(nums):
    n = len(nums)
    answer = [0] * n

    for i in range(n):
        product = 1

        for j in range(n):
            if i != j:
                product *= nums[j]

        answer[i] = product

    return answer


n = int(input())
nums = list(map(int, input().split()))

result = product_except_self(nums)

for x in result:
    print(x, end=" ")