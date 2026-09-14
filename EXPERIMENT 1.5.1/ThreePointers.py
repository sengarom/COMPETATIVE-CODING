class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n = int(input("Enter number of nodes: "))

head = None
tail = None

for i in range(n):
    value = int(input("Enter node: "))
    newNode = Node(value)

    if head is None:
        head = newNode
        tail = newNode
    else:
        tail.next = newNode
        tail = newNode

if head is None or head.next is None:
    temp = head
else:
    odd = head
    even = head.next
    evenHead = even

    while even is not None and even.next is not None:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = evenHead

    temp = head

print("Result:")
while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next