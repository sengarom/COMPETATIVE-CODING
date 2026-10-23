class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Find path from root to target node
    def findPath(self, root, target, path):
        if root is None:
            return False

        path.append(root)  # Add current node to path

        # Target found
        if root.val == target:
            return True

        # Search in left or right subtree
        if (self.findPath(root.left, target, path) or
                self.findPath(root.right, target, path)):
            return True

        path.pop()  # Remove node if target not found
        return False

    def lowestCommonAncestor(self, root, p, q):
        path1 = []
        path2 = []

        # Find paths from root to p and q
        self.findPath(root, p.val, path1)
        self.findPath(root, q.val, path2)

        lca = None
        i = 0

        # Compare both paths
        while (i < len(path1) and i < len(path2)
               and path1[i] == path2[i]):
            lca = path1[i]  # Store last common node
            i += 1

        return lca


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

    # Find nodes using breadth-first traversal
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