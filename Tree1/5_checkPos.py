'''
นำ code จากข้อ 1 มาเปลี่ยนเป็น
เพื่อหาว่าค่าแรกที่ใส่เข้าไปอยู่ที่ตำแหน่งใดใน BST (Root, Inner, leaf)
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if (self.root == None) :
            self.root = Node(data)
            return
        else:
            cur = self.root
            while True:
                if data < cur.data:
                    if cur.left == None:
                        cur.left = Node(data)
                        break
                    else:
                        cur = cur.left
                else:
                    if cur.right == None:
                        cur.right = Node(data)
                        break
                    else:
                        cur = cur.right
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
    def checkpos(self,n):
        cur = self.root
        while cur is not None and n != cur.data:
            if n > cur.data:
                cur = cur.right
            elif n < cur.data:
                cur = cur.left
        if cur is None:
            print("Not exist")
        elif cur is self.root:
            print("Root")
        elif cur.left is not None or cur.right is not None:
            print("Inner")
        else:
            print("Leaf")
        

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
T.checkpos(inp[0])