class Node:
    def __init__(self, data,next = None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        count = 0
        current_node = self.head
        while(current_node != None):
            count += 1
            current_node = current_node.next
        return count

    def append(self, data): 
        p = Node(data)
        if self.head == None:
            self.head = p
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = p

    def printList(self): 
        p = self.head
        print('link list : ')
        while p != None:
            print(p.data," -> ", end = '')
            p = p.next
            
    def insert(self, index, data):
        p = Node(data)
        if index < 0:
            print('Data cannot be added')
        if index == 0: #ADD Head
            p.next = self.head
            self.head = p
        else:    
            temp = self.head
            for i in range(0, index):
                if(temp != None):
                    temp = temp.next   
            if(temp != None):
                p.next = temp.next
                temp.next = p 
            else:
                print("\nThe previous node is null.") 
    

inp = input('Enter Input :  ').split(',')
llist = LinkedList()

i = 0
for i in range(len(inp)):
    if i == 0:
        if inp[i] == ' ':
            print('List is empty')
            llist = []
        else:
            llist = inp[0].split()
            print(f'link list : {llist}')
    elif i > 0:
        index,data = inp[i].split(':')
        print(f'index = {index} and data = {data}')
        llist.insert(int(index),int(data))
        #llist.printList()
        print(llist)
    if llist.size() > index:
        print('Data cannot be added')

   
    


