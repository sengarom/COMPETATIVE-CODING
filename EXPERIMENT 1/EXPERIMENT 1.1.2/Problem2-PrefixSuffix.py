def product_except_self(nums):
    n = len(nums)
    res = [1] * n

    pre = 1
    for i in range(n):
        res[i] = pre
        pre *= nums[i]

    suf = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suf
        suf *= nums[i]

    return res


n = int(input())
nums = list(map(int, input().split()))

ans = product_except_self(nums)

print("Output:", *ans)