# Define the Node class first
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

# Then define the levelOrder function
def levelOrder(root):
    if not root:
        return

    q = []
    q.append(root)

    while q:
        n = q.pop(0)
        print(n.info, end=" ")

        if n.left is not None:
            q.append(n.left)
        if n.right is not None:
            q.append(n.right)

# Now create the binary tree using the Node class
# 🔧 Building a sample binary tree:
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

# Call levelOrder
print("Level Order Traversal:")
levelOrder(root)
