#largest rectangle in histogram brute force

def largest_rectangle(heights):
    max_area = 0
    n = len(heights)

    for i in range(n):
        min_height = heights[i]
        for j in range(i, n):
            min_height = min(min_height, heights[j])
            area = min_height * (j - i + 1)
            max_area = max(max_area, area)

    return max_area

print("enter number of values:")
n = int(input())
heights = []
print("enter the heights:")
for k in range(n):
    heights.append(int(input()))

result = largest_rectangle(heights)
print("largest rectangle:", result)