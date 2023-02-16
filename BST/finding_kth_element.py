class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder_traversal(node):
    if node is None:
        return []
    return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

def kth_smallest(node, k):
    inorder_list = inorder_traversal(node)
    if k > len(inorder_list):
        return None
    return inorder_list[k-1]

def kth_largest(node, k):
    inorder_list = inorder_traversal(node)
    if k > len(inorder_list):
        return None
    return inorder_list[-k]

root = Node(25)
root.left = Node(15)
root.right = Node(50)
root.left.left = Node(10)
root.left.right = Node(22)
root.right.left = Node(35)
root.right.right = Node(70)

print(kth_smallest(root, 3))
print(kth_largest(root, 2))
