''''กฤษฎาได้ค้นพบเม็ดถั่ววิเศษที่เมื่อโยนลงดินแล้วถั่วจะสามารถเติบโตขึ้นและกลายเป็น Binary Search Tree (BST) ได้ 
โดยงานของนักศึกษาก็คือนักศึกษาจะต้องสร้าง BST ตามลำดับของข้อมูลนำเข้าซึ่งเป็นตัวเลขจำนวนเต็มที่ไม่ซ้ำกันเลย 
โดยในการใส่ค่าในแต่ละครั้งจะกลับมาที่ Root of BST เสมอ  แล้วท่องต้นไม้ไปทางซ้ายด้วยคำสั่ง "L" หรือท่องต้นไม้ไปทางขวาด้วยคำสั่ง "R" 
จนกว่าจะถึงตำแหน่งที่เหมาะสมที่จะใส่ข้อมูลแล้วจึงพิมพ์ "*" เพื่อใส่ข้อมูลลงไปในต้นไม้  
จงเขียนโปรแกรมเพื่อแสดงคำสั่งการท่องต้นไม้ในการใส่ข้อมูลทีละค่าตามลำดับของข้อมูลนำเข้า
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        newNode = Node(data)
        temp = ''
        if self.root == None:
            self.root = newNode
            return '*'
        else:
            r = self.root
            while True:
                if data < r.data:
                    if r.left == None:
                        r.left = newNode
                        temp += 'L*'
                        return temp
                    else:
                        r = r.left
                        temp += 'L'
                else:
                    if r.right == None:
                        r.right = newNode
                        temp += 'R*'
                        return temp
                    else:
                        r = r.right
                        temp += 'R'

T = BST()
com = [int(i) for i in input('Enter Input : ').split()]
for i in com:
    print(T.insert(i))

