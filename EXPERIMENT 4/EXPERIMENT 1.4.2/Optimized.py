class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def detectCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


n = int(input("Enter number of nodes: "))

nodes = []

for i in range(n):
    value = int(input(f"Enter value of node {i + 1}: "))
    nodes.append(Node(value))

# Connect nodes
for i in range(n - 1):
    nodes[i].next = nodes[i + 1]

head = nodes[0] if n > 0 else None

pos = int(input("Enter cycle position (-1 for no cycle): "))

if pos != -1:
    nodes[-1].next = nodes[pos]

if detectCycle(head):
    print("Cycle detected")
else:
    print("No cycle detected")