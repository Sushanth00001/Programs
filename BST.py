class Node:
    def __init__(self, key):  # Fix: Should be __init__, not _init_
        self.left = None      # Fix: should be = not +
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)  # Fix: Node(key), not None(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

# Using correct argument format (key:3 → 3)
r = Node(7)
r = insert(r, 3)
r = insert(r, 5)
r = insert(r, 6)
r = insert(r, 4)
r = insert(r, 1)

inorder(r)
