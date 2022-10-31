''''
ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ และหาค่าที่น้อยกว่าค่าที่รับเข้ามาของ Binary Search Tree

***** ห้ามใช้ Built-in Function เช่น min() , max() , sort() , sorted()
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
    
    def below(self,node,data):
        if node == None:
            return ''
        belowlst = ''
        belowlst += self.below(node.left,data)
        # print(belowlst)
        if int(node.data) < int(data):
            belowlst += str(node.data) + ' '
        belowlst += self.below(node.right,data)
        return belowlst
                 
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
tree,below = input('Enter Input : ').split('|')
t = [int(i) for i in tree.split()]
for i in t:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
belowList = T.below(root,below)
if belowList == '':
    print(f'Below {below} : Not have')
else:
    print(f'Below {below} : {belowList}')