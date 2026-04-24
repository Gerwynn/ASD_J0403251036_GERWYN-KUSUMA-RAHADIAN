#=======================================================================================
# Nama    : Gerwyn Kusuma Rahadian
# NIM     : J0403251036
# Kelas   : A1
#=======================================================================================

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data 

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def inorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.inorder_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.inorder_traversal()
        return elements
    
    def preorder_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preorder_traversal()
        if self.right:
            elements += self.right.preorder_traversal()
        return elements
    
    def postorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.postorder_traversal()
        if self.right:
            elements += self.right.postorder_traversal()
        elements.append(self.data)
        return elements

#NIM : J0403251036
#Data = [36, 16, 56, 6, 26, 46, 66, 21]
root = Node(36)
root.insert(16)
root.insert(56)
root.insert(6)
root.insert(26)
root.insert(46)
root.insert(66)
root.insert(21)

print("Nama     : Gerwyn Kusuma Rahadian"
      "\nNIM      : J0403251036"
      "\n===========================================================")
print("Data = [36, 16, 56, 6, 26, 46, 66, 21]")
print("Inorder Traversal:", root.inorder_traversal())
print("Preorder Traversal:", root.preorder_traversal()) 
print("Postorder Traversal:", root.postorder_traversal())