'''
ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ
และให้หา พ่อ(father node) ของ node ที่กำหนด
'''
class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
        
def father(node,data,parent):
    if node == None:
        return ''
    if (node.data == data):
        if parent == -1:
            print(f'None Because {data} is Root')
        else:
            print(parent)
    else:
        father(node.left, data, node.data)
        father(node.right, data, node.data)
        
    # global isParent
    # if node == None:
    #     return ''
    
    # belowlst = ''
    # if int(node.data) == int(data):
    #     belowlst += str(node.data) + ' '
    #     isParent = True
    # belowlst += father(node.left,data)
    # # print(belowlst)
    # belowlst += father(node.right,data)
    # if isParent :
    #     return node.data + " "

tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
 
isParent = False
isFound = 0

for e in data[0].split():

    tree.create(e)
    if e == data[1]:
        isFound += 1
printTree90(tree.root)
parent = father(tree.root,data[1],-1)

if isFound == 0:
    print('Not Found Data')



