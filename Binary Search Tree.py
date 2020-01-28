#Search in BST
def BST(root,key):  
    if root is None or root.val == key: 
        return root 
    elif root.val < key: 
        return BST(root.right,key)  
    else:
        return BST(root.left,key) 
    
#Insertion in BST
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 
  
r = Node(100) 
insert(r,Node(50)) 
insert(r,Node(60)) 
insert(r,Node(20)) 
insert(r,Node(30)) 
insert(r,Node(40)) 
insert(r,Node(10))

def Preorder(root):
    if root:
        print(root.value)
        Preorder(root.left)  
        Preorder(root.right) 
Preorder(r)