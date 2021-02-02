class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        if self.root:
            self.insertNode(data,self.root)
        else:
            self.root=Node(data)
    def insertNode(self,data,node):
        if node.data > data:
            if node.left:
                self.insertNode(data,node.left)
            else:
                node.left=Node(data)
        else:
            if node.right:
                self.insertNode(data,node.right)
            else:
                node.right=Node(data)
    def traverse(self):
        if self.root:
            print("INorder")
            self.inorder(self.root)
            print("PREorder")
            self.preorder(self.root)
    def inorder(self,node):
        if node.left:
            self.inorder(node.left)
        print(node.data,end=" ")
        if node.right:
            self.inorder(node.right)
    def remove(self,data):
        if self.root:
            self.removeNode(data,self.root)
    def removeNode(self,data,node):
        if not node:
            return node
        if node.data<data:
            self.removeNode(data,node.right)
        elif node.data>data:
            self.removeNode(data,node.left)
        else:
            if not node.left and not node.right:
                print("leaf Node")
                del node
                return None
            if not node.left:
                print("remove right leaf node")
                temp=node.right
                del node
                return temp
            if not node.right:
                print("remove left leaf node")
                temp=node.left
                del node
                return temp
            print("removing node with two child ")
            temp=self.getPredecessor(node.left)
            node.data=temp.data
            node.left=self.removeNode(temp.data,node.left)
        return node
    def getPredecessor(self,node):
        if node.right:
            return self.getPredecessor(node.right)
        return node
    def preorder(self,node):
        print(node.data,end=" ")
        if node.left:
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)
a=BST()
a.insert(3)
a.insert(2)
a.insert(1)
a.insert(4)
a.insert(6)
a.traverse()
a.remove(3)
a.traverse()