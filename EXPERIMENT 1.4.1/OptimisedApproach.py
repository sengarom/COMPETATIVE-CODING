class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def createLinkedList(values):
    if not values:
        return None

    head = Node(values[0])
    curr = head

    for value in values[1:]:
        curr.next = Node(value)
        curr = curr.next

    return head


def is_palindrome(head):

    if head is None or head.next is None:
        return True

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow.next

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    first = head
    second = prev

    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next

    return True

n = int(input())

print("Enter the values of the linked list:")
val = []

for i in range(n):
    val.append(int(input()))

head = createLinkedList(val)

if is_palindrome(head):
    print("True")

else:
    print("False")