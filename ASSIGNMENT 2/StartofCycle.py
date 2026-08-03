class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_start(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = head

            while slow != fast:
                slow = slow.next
                fast = fast.next

            return slow

    return None


n = int(input("Enter number of nodes: "))
values = list(map(int, input("Enter node values: ").split()))

nodes = []

for value in values:
    nodes.append(Node(value))

for i in range(n - 1):
    nodes[i].next = nodes[i + 1]

pos = int(input("Enter cycle position (-1 for no cycle): "))

if pos != -1:
    nodes[-1].next = nodes[pos]

head = nodes[0]

start = find_start(head)

if start:
    print("Cycle starts at:", start.data)
else:
    print("No cycle")