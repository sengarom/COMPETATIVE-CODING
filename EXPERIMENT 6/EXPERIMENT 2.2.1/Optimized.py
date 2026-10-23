class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # Return if tree is empty or current node is p or q
        if root is None or root == p or root == q:
            return root

        # Search for p or q in the left subtree
        left = self.lowestCommonAncestor(root.left, p, q)

        # Search for p or q in the right subtree
        right = self.lowestCommonAncestor(root.right, p, q)

        # Both nodes found in different subtrees
        if left is not None and right is not None:
            return root

        # Return the side where a node was found
        if left is not None:
            return left

        return right


def main():
    # Create sample binary tree
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    p_value = int(input("Enter value of p: "))
    q_value = int(input("Enter value of q: "))

    # Find nodes p and q using breadth-first traversal
    nodes = [root]
    p = None
    q = None

    for current in nodes:
        if current.val == p_value:
            p = current

        if current.val == q_value:
            q = current

        if current.left is not None:
            nodes.append(current.left)

        if current.right is not None:
            nodes.append(current.right)

    if p is None or q is None:
        print("One or both nodes were not found.")
        return

    obj = Solution()
    lca = obj.lowestCommonAncestor(root, p, q)

    if lca is not None:
        print("Lowest Common Ancestor:", lca.val)
    else:
        print("Lowest Common Ancestor not found.")


if __name__ == "__main__":
    main()