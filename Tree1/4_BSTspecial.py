'''
ให้น้องรับ input เข้ามาและสร้าง Binary Search Tree ต่อมาให้แสดงผลแบบ 
Preorder , Inorder , Postorder และ Breadth First Search ตามลำดับ
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
    
    def Inorder(self, node):
        if node != None:
            self.Inorder(node.left)
            print(node,end = ' ')
            self.Inorder(node.right)
    
    def Preorder(self, node):
        if node != None:
            print(node,end = ' ')
            self.Preorder(node.left)
            self.Preorder(node.right)
            
    def Postorder(self, node):
        if node != None:
            self.Postorder(node.left)
            self.Postorder(node.right)
            print(node,end = ' ')
            
    def Breadth(self, root=None):
        if root is None:
            return
        queue = [root]
        while len(queue) > 0:
            cur_node = queue.pop(0)
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)
            print(queue)
            
def printLevel(root, level):

    if root is None:
        return False
 
    if level == 1:
        print(root.data, end=' ')
        return True
 
    left = printLevel(root.left, level - 1)
    right = printLevel(root.right, level - 1)
 
    return left or right
 
def breadth(root):
    level = 1
    while printLevel(root, level):
        level = level + 1

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
    
print(f'Preorder : ',end = '')
T.Preorder(root)
print()
    
print(f'Inorder : ',end = '')
T.Inorder(root)
print()

print(f'Postorder : ',end = '')
T.Postorder(root)
print()

print(f'Breadth : ',end = '')
breadth(root)
print()
