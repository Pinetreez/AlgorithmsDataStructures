# Check if a given list of numbers represents a max-heap or not

# Basic binary tree
class Node:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

# Returns true if the array is a max-heap
def _isMaxHeap(node):

    if node is None or (node.rightChild and node.leftChild is None):
        return True
    
    if node.leftChild:
        if node.leftChild.key >= node.key:
            return False
        
    if node.rightChild:
        if node.rightChild.key >= node.key:
            return False
    
    return _isMaxHeap(node.leftChild) and _isMaxHeap(node.rightChild)
   

def isMaxHeap(node):
    if _isMaxHeap(node):
        return "Yes"
    else:
        return "No"

# Test code
if __name__ == '__main__':
    # Example 1: Should be a max-heap
    root1 = Node(90)
    root1.leftChild = Node(36)
    root1.rightChild = Node(18)
    root1.leftChild.leftChild = Node(8)
    root1.leftChild.rightChild = Node(25)
    root1.rightChild.leftChild = Node(7)
    root1.rightChild.rightChild = Node(1)

    # Example 2: Should not be a max-heap
    root2 = Node(90)
    root2.leftChild = Node(36)
    root2.rightChild = Node(18)
    root2.leftChild.leftChild = Node(98)  # This violates the max-heap property
    root2.leftChild.rightChild = Node(25)
    root2.rightChild.leftChild = Node(7)
    root2.rightChild.rightChild = Node(1)

    # Example 3: Should not be a max-heap
    root3 = Node(90)
    root3.leftChild = Node(36)
    root3.rightChild = Node(18)
    root3.leftChild.leftChild = Node(8)
    root3.leftChild.rightChild = Node(25)
    root3.rightChild.leftChild = Node(7)
    root3.rightChild.rightChild = Node(20)  # This violates the max-heap property

    print("Is root1 a max-heap? ", isMaxHeap(root1))  # Expected result: Yes
    print("Is root2 a max-heap? ", isMaxHeap(root2))  # Expected result: No
    print("Is root3 a max-heap? ", isMaxHeap(root3))  # Expected result: No