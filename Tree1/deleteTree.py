class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
    
class BST():
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            cur = self.root
            while True:
                if data > cur.data:
                    if cur.right == None:
                        cur.right = Node(data)
                        break
                    else:
                        cur = cur.right
                else:
                    if cur.left == None:
                        cur.left = Node(data)
                        break
                    else:
                        cur = cur.left
        return self.root
    
    def delete(self,r,data):
        if self.root.left == None and self.root.right == None and self.root.data == data:
            self.root = None
        elif self.root.left == None and self.root.data == data:
            self.root = self.root.right
        elif self.root.right == None and self.root.data == data:
            self.root = self.root.left

        if r is None:
            print("Error! Not Found DATA")
            return
        if r.data != data:
            if r.data > data:
                r.left = self.delete(r.left,data)
            else:
                r.right = self.delete(r.right,data)
        else:
            if r.left is None: #1child with left none
                r = r.right
                return r
            elif r.right is None: #1child with right none
                r = r.left
                return r
            else: 
                cur = r.right #inorder successor
                while cur.left != None: 
                    cur = cur.left 
                r.data = cur.data
                r.right = self.delete(r.right,cur.data) 
        return r
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1) 
            
T = BST()
inp = input('Enter Input : ').split(',')

for i in inp:
    if i[0] == 'i':
        print(f'insert {i[2]}')
        root = T.insert(i[2])
        T.printTree(root)
    elif i[0] == 'd':
        print(f'delete {i[2]}')
        T.delete(root,i[2])
        T.printTree(root)