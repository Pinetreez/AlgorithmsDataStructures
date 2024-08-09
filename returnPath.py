# Given a BST and a number k, return the path


from BST import BST, Node

def get_path(root, k):

    if not root:
        return None
    
    if k == root.key:
        return [root.key]

    if k > root.key:
        rightPath = get_path(root.rightChild, k)
        if rightPath:
            return [root.key] + rightPath
        
    if k < root.key:
        leftPath = get_path(root.leftChild, k)
        if leftPath:
            return [root.key] + leftPath
    return None





if __name__ == "__main__":
    myTree = BST()
    myTree[10] = "A"
    myTree[8] = "B"
    myTree[12] = "C"
    myTree[3] = "D"
    myTree[9] = "E"
    myTree[22] = "F"

    k = 10  
    print(get_path(myTree.root, k))  # Expected result: [10]

    k = 22  
    print(get_path(myTree.root, k))  # Expected result: [10, 12, 22]

    k = 9  
    print(get_path(myTree.root, k))  # Expected result: [10, 8, 9]

    k = 3  
    print(get_path(myTree.root, k))  # Expected result: [10, 8, 3]

    k = 5  
    print(get_path(myTree.root, k))  # Expected result: None, since 5 is not in the tree