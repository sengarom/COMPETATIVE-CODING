Then going further like we need to draw how we move using the sense of what do we character, so this should be nice to and it should be on its whether someone says you works experiment number two, it should be for whether it's where you meant for attachment. So once you go to some new concept, this is hash matrism here, so you will have to first explain the tash map what it does and what it is, then how it can do what so in then you will have to go for the slide in your file. Also, since this is a new observed in the flow of the answer, slightly videos are a new answer. If you must say what sliding you do is then how will you plan if someone is able to explain a recent and is able to relearn how to use, relearn how to use slides, and that is something as we should be able to prove in which explain a basis for just do it at a sinks already done as a codedef product_except_self(nums):
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