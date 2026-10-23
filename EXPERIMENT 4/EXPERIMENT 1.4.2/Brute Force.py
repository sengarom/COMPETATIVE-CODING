class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detectCycle(head):
    visited = set()
    current = head

    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next

    return False

n = int(input("Enter number of nodes: "))
nodes = []
for i in range(n):
    value = int(input(f"Enter value of node {i + 1}: "))
    nodes.append(Node(value))

for i in range(n - 1):
    nodes[i].next = nodes[i + 1]

head = nodes[0]

pos = int(input("cycle pos:"))

if pos != -1:
    nodes[-1].next = nodes[pos]

if detectCycle(head):
    print("Cycle detected")
else:
    print("No cycle detected")


