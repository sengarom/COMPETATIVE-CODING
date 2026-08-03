def largest_rectangle(heights):

    heights.append(0)

    stack = []
    max_area = 0

    for i in range(len(heights)):

        while len(stack) > 0 and heights[i] < heights[stack[-1]]:

            top = stack.pop()

            height = heights[top]

            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] - 1

            area = height * width

            if area > max_area:
                max_area = area

        stack.append(i)

    heights.pop()

    return max_area


print("Enter number of bars:")
n = int(input())

heights = []

print("Enter the heights:")
for i in range(n):
    value = int(input())
    heights.append(value)

result = largest_rectangle(heights)

print("Largest Rectangle =", result)