class Queue():
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enQueue(self,ele):
        self.items.append(ele)

    def deQueue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            return "Empty"
    
    def insert(self,index,ele):
        return self.items.insert(index,ele)        
    
    def pos(self,ele):
        for item in self.items:
            if(item == ele):
                return self.items.index(ele)

    def peek(self):
        return self.items[-1]
        
    def __str__(self):
        return str(self.items)

inp = input('Enter Input : ').split('/')
addID = inp[0].split(',')
operation = inp[1].split(',')
q = Queue()
dict = {}

for i in addID:
    Id,sec = i.split()
    #print(f'id = {Id},sec = {sec}')
    dict[sec] = Id


for i in operation:
    if i[0] == 'D':
        print(q.deQueue())
    elif i[0] == 'E':
        operator,Iden = i.split()
        temp = ""

        for item in q.items:
            if(dict.get(temp) == dict.get(Iden) and dict.get(item) != dict.get(Iden)):# check before and now item
                q.insert(q.pos(item),Iden)
                break;
            elif(item == q.peek()): #enque last
                q.enQueue(Iden)
                break;
            temp = item

        if q.isEmpty():
            q.enQueue(Iden)
