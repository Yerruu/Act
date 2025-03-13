class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# in order traversal
def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.value, end=" ")
        in_order_traversal(root.right)   

# pre order traversal     
def pre_order_traversal(joshz):
    if joshz:
        print(joshz.value, end=" ")
        pre_order_traversal(joshz.left)
        pre_order_traversal(joshz.right)

# post order traversal
def post_order_traversal(david):
    if david:
        post_order_traversal(david.left)
        post_order_traversal(david.right)
        print(david.value, end=" ")

def swapthetree(root):
    if root:
        root.left, root.right = root.right, root.left
        swapthetree(root.left)
        swapthetree(root.right)
        print(root.value, end=" ")



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("In order traversal:")
in_order_traversal(root)    

print("\nPre order traversal:")
pre_order_traversal(root)

print("\nPost order traversal:")
post_order_traversal(root)

print("\nSwapped tree:")
swapthetree(root)

print("\nPre order traversal: Swapped edition")
pre_order_traversal(root)

print("\nIn order traversal: Swapped edition")
in_order_traversal(root)

print("\nPost order traversal: Swapped edition")
post_order_traversal(root)