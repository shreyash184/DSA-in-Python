

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None 

def inorderTraversal(root):  
  if root:  
    inorderTraversal(root.left)  
    print(root.val, end = " ")  
    inorderTraversal(root.right)  

def search(root, x):
    if root is None:
        return root 
    
    if root.val == x:
        return root
    
    if root.val > x:
        return search(root.left, x)
    else:
        return search(root.right, x)
    
    return -1

def insert_in_bst(root, x):
    if root is None:
        return Node(x)
    else:
        if root.val == x:
            return root 
        elif root.val < x:
            root.right = insert_in_bst(root.right, x)
        else:
            root.left = insert_in_bst(root.left, x)
    return root
    
root = Node(9)
root.left = Node(1)
root.right = Node(10)
root.left.left = Node(0)  
root.left.right = Node(3)  
root.left.right.right = Node(4) 

x = 4
v = search(root, x)
i = insert_in_bst(root, 5)
inorderTraversal(i)