class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def detect_cycle(head):
    visited = set()

    while head:
        if head in visited:
            return True
        visited.add(head)
        head = head.next

    return False


n = int(input("Enter number of nodes: "))
values = list(map(int, input("Enter node values: ").split()))

head = Node(values[0])
current = head

for i in range(1, n):
    current.next = Node(values[i])
    current = current.next

if detect_cycle(head):
    print("Cycle detected")
else:
    print("No cycle detected")