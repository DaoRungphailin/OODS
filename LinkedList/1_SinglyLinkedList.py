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
        temp = self.head
        while(temp != None):
            count += 1
            temp = temp.next
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
        txt = ''
        p = self.head
        while p != None:
            if p.next == None:
                txt += p.data
                break;
            txt += str(p.data) + '->'
            p = p.next
       # removing trailing commas
        return txt
            
    def insert(self, index, data):
        p = Node(data)
        if index < 0:
            print('Data cannot be added')
        if index == 0: #ADD Head
            p.next = self.head
            self.head = p
        else:    
            temp = self.head
            for i in range(1, index):
                if(temp != None):
                    temp = temp.next   
            if(temp != None):
                p.next = temp.next
                temp.next = p 
            else:
                print("Data cannot be added") 
    

inp = input('Enter Input : ').split(',')
llist = LinkedList()

i = 0

if inp[0] == '':
    print('List is empty')
else:
    for i in inp[0].split():
        llist.append(i)
    
    print(f'link list : {llist.printList()}')

for i in range(len(inp)):
    if i > 0:
        index,data = inp[i].split(':')

        if int(index) >= 0 and int(index) <= llist.size():
            print(f'index = {int(index)} and data = {data}')
            llist.insert(int(index),data)
            print(f'link list : {llist.printList()}')
        else:
            print('Data cannot be added')
            if llist.isEmpty():
                print('List is empty')
            else:
                print(f'link list : {llist.printList()}')

   
    


