class Node:
    def __init__(self,data,next = None):
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

    def remove(self,data):
        current = self.head;
        previous = None;
        while current is not None:
            if current.data == data:
            # if this is the first node (head)
                if previous is not None:
                    previous.nextNode = current.nextNode
                else:
                    self.head = current.nextNode
            previous = current
            current = current.nextNode;

    def printList(self): 
        txt = ''
        p = self.head
        while p != None:
            txt += str(p.data) + '->'
            p = p.next
       # removing trailing commas
        txt = txt.strip("->")
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
for i in inp:
    inpu = inp.split(' ')
for i in inpu:
    if inpu[0] == 'I':
        command,word = inpu[0].split()
        print(f'command = {command} word = {word}')