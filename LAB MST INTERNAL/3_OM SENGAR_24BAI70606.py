s = input("Enter a string: ").strip()
n = len(s)
max_length = 0
char_set = set()
left = 0

for right in range(n):
    while s[right] in char_set:
        char_set.remove(s[left])
        left += 1

    char_set.add(s[right])
    max_length = max(max_length, right - left + 1)

print(max_length)