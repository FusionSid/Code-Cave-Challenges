# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode) -> TreeNode:
    def invert(node):
        if not node:
            return

        invert(node.left)
        invert(node.right)

        node.left, node.right = node.right, node.left

    invert(root)

    return root


# Testing
def create_list(tree):
    items = []
    queue = [tree]

    while queue:
        copy = queue[:]
        queue = []

        for item in copy:
            items.append(item.val)
            queue.append(item.left)
            queue.append(item.right)

        if all((x is None for x in queue)):
            break

    return items


root1 = TreeNode(1, TreeNode(2), TreeNode(3))
print("1\nTree:", create_list(root1))
result1 = invert_tree(root1)
print("Inverted:", create_list(result1))

root2 = TreeNode(
    1, TreeNode(7, TreeNode(4), TreeNode(2)), TreeNode(3, TreeNode(6), TreeNode(9))
)
print("\n2\nTree:", create_list(root2))
result2 = invert_tree(root2)
print("Inverted:", create_list(result2))

root3 = TreeNode()
print("\n3\nTree:", create_list(root3))
result3 = invert_tree(root3)
print("Inverted:", create_list(result3))
