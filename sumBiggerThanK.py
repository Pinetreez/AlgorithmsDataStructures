#Given a BST return the sum of all the elements in the BST greater than k

#      10
#     /  \
#    8 	  12
#   / \     \
#  3   9    22
#

from BST import BST


def sumBigger(root, k):
    if root is None:
        return 0
    
    if k > root.key:
        return sumBigger(root.rightChild, k)
    
    if k < root.key:
        return root.key + sumBigger(root.leftChild, k) + sumBigger(root.rightChild, k)
    
    return None
    



if __name__ == "__main__":

    myTree = BST()
    myTree[10] = "A"
    myTree[8] = "B"
    myTree[12] = "C"
    myTree[3] = "D"
    myTree[9] = "E"
    myTree[22] = "F"

    k = 5  #result 61
    print(sumBigger(myTree.root, k))

    k = 11 #result 34
    print(sumBigger(myTree.root, k))
