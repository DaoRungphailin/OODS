class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class AVL:

    def __init__(self):
        self.root = None
    
    def insert(self,node,data):
        if node == None:
            return Node(data)
        if data < node.data:
            node.left = self.insert(node.left,data)
        elif data >= node.data:
            node.right = self.insert(node.right,data)
        balance = self.height(node.left) - self.height(node.right)
        #L L
        if balance > 1 and data < node.left.data :
            return self.rightRotate(node)
        #R R
        if balance < -1 and data >= node.right.data :
            return self.leftRotate(node)
        #L R
        if balance > 1 and data >= node.left.data :
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        #R L
        if balance < -1 and data < node.right.data :
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        return node
        
    def height(self,node):
        if node == None:
            return 0
        height_left = self.height(node.left)
        height_right = self.height(node.right)
        if height_left > height_right:
            return height_left + 1
        else:
            return height_right + 1

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        return y
    
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        return y
    
avl = AVL()
lists = list(map(int,input("Enter Input : ").split(" ")))
for i in lists:
    print("Insert : "+"( "+str(i)+" )")
    avl.root = avl.insert(avl.root,i)
    avl.printTree(avl.root)
    print("--------------------------------------------------")
    