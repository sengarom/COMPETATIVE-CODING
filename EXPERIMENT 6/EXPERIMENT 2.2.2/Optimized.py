class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root, p):
        successor = None

        while root is not None:
            # Current node is smaller than or equal to p
            if p.val >= root.val:
                root = root.right  # Move right

            # Current node is greater than p
            else:
                successor = root  # Store possible successor
                root = root.left  # Search for a smaller greater value

        return successor


def main():
    # Create sample BST
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)

    p_value = int(input("Enter value of p: "))

    # Find node p using breadth-first traversal
    nodes = [root]
    p = None

    for current in nodes:
        if current.val == p_value:
            p = current
            break

        if current.left is not None:
            nodes.append(current.left)

        if current.right is not None:
            nodes.append(current.right)

    if p is None:
        print("Node not found.")
        return

    obj = Solution()
    successor = obj.inorderSuccessor(root, p)

    if successor is not None:
        print("In-order Successor:", successor.val)
    else:
        print("In-order Successor: NULL")


if __name__ == "__main__":
    main()