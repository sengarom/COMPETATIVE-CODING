class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_linked_list(arr):
    if not arr:
        return None

    head = Node(arr[0])
    curr = head

    for value in arr[1:]:
        curr.next = Node(value)
        curr = curr.next

    return head


def is_palindrome(head):
    vals = []
    curr = head

    while curr:
        vals.append(curr.val)
        curr = curr.next

    left = 0
    right = len(vals) - 1

    while left < right:
        if vals[left] != vals[right]:
            return False
        left += 1
        right -= 1

    return True


n = int(input("Enter the number of nodes: "))

print("Enter the values:")
arr = []
for i in range(n):
    arr.append(int(input()))


head = create_linked_list(arr)


if is_palindrome(head):
    print("True")
else:
    print("False")