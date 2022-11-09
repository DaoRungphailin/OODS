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
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1) 
        
    def min(self):
        cur = self.root
        while cur.left != None:    
            cur = cur.left           
        return cur.data

    def max(self):
        cur = self.root
        while cur.right != None:    
            cur = cur.right           
        return cur.data
    
    def red(self,cur,key):
        if cur.data != None:
            if(key < cur.data ):
                cur.data = cur.data*3
            if(cur.right != None):
                self.red(cur.right,key)
            if(cur.left != None):
                self.red(cur.left,key)
    
    def below(self,cur,key,below):
        below =''
        if cur.data != None:
            
            if cur.data < key :
                # print(cur.data)
                below += str(cur.data) + ' '
                print(f'Below : {below}')
            if(cur.right != None):
                self.below(cur.right,key)
            if(cur.left != None):
                self.below(cur.left,key)
        return below

T = BST()
inpu,key = input('Enter Input : ').split('|')
inp = [int(i) for i in inpu.split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------')
below = T.below(root,int(key))
print(f'Below : {below}')
# print('--------------------------------------------')
# T.red(root,int(key))
# T.printTree(root)
# print('--------------------------------------------')
# print(f'Min : {T.min()}')
# print(f'Min : {T.max()}')