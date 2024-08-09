#Print the order traversals (3 different ways)

class Node:
    # WARNING: DO NOT MODIFY THIS INITIALIZATION METHOD!
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

# In-order traversal
def inorder_traversal(root):
    result = []
    if root:
        result.extend(inorder_traversal(root.leftChild))
        result.append(root.key)
        result.extend(inorder_traversal(root.rightChild))
    return result


# Pre-order traversal
def preorder_traversal(root):
    result = []
    if root:
        result.append(root.key)
        result.extend(preorder_traversal(root.leftChild)) #extend = appends multiple elements
        result.extend(preorder_traversal(root.rightChild))
    return result

# Post-order traversal
def postorder_traversal(root):
    result = []
    if root:
        result = postorder_traversal(root.leftChild)
        result = result + postorder_traversal(root.rightChild)
        result.append(root.key)
    return result

# Test code
if __name__ == '__main__':
    # WARNING: DO NOT MODIFY THE TREE STRUCTURE!
    root1 = Node("A")
    root1.leftChild = Node("B")
    root1.leftChild.leftChild = Node("D")
    root1.leftChild.leftChild.leftChild = Node("H")
    root1.leftChild.leftChild.rightChild = Node("I")
    root1.leftChild.rightChild = Node("E")
    root1.rightChild = Node("C")
    root1.rightChild.leftChild = Node("F")
    root1.rightChild.rightChild = Node("G")

    # WARNING: DO NOT MODIFY THE TREE STRUCTURE!
    root2 = Node("A")
    root2.leftChild = Node("B")
    root2.leftChild.leftChild = Node("D")
    root2.leftChild.rightChild = Node("E")
    root2.rightChild = Node("C")
    root2.rightChild.rightChild = Node("G")

    # WARNING: DO NOT MODIFY THE TREE STRUCTURE!
    root3 = Node("A")
    root3.leftChild = Node("B")
    root3.leftChild.leftChild = Node("D")
    root3.leftChild.leftChild.leftChild = Node("H")
    root3.leftChild.leftChild.rightChild = Node("I")
    root3.leftChild.rightChild = Node("E")
    root3.rightChild = Node("C")

    inorder = []
    print("In-order traversal of root1:", inorder_traversal(root1))
    print("Pre-order traversal of root1:", preorder_traversal(root1))
    print("Post-order traversal of root1:", postorder_traversal(root1))

    print("In-order traversal of root2:", inorder_traversal(root2))
    print("Pre-order traversal of root2:", preorder_traversal(root2))
    print("Post-order traversal of root2:", postorder_traversal(root2))

    print("In-order traversal of root3:", inorder_traversal(root3))
    print("Pre-order traversal of root3:", preorder_traversal(root3))
    print("Post-order traversal of root3:", postorder_traversal(root3))
