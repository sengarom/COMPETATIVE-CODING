class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Store nodes in in-order sequence
    def inorder(self, root, order):
        if root is None:
            return

        self.inorder(root.left, order)  # Visit left subtree
        order.append(root)              # Store current node
        self.inorder(root.right, order) # Visit right subtree

    def inorderSuccessor(self, root, p):
        order = []

        # Generate sorted in-order sequence
        self.inorder(root, order)

        # Find p and return the next node
        for i in range(len(order)):
            if order[i] == p:
                if i + 1 < len(order):
                    return order[i + 1]

                return None  # p is the largest node

        return None


def main():
    # Create sample BST
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)

    p_value = int(input("Enter value of p: "))

    # Find node p
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