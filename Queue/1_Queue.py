class Queue():
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self,i):
        self.items.append(i)

    def deQueue(self):    
        if not self.isEmpty():
            return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
    
    def lst2Q(self,string):
        return 'Empty' if self.isEmpty() else string.join(self.items)
        # if self.isEmpty():
        #     return 'Empty'
        # return string.join(self.items)

inp = list(input("Enter Input : ").split(','))
q = Queue()
dq = Queue()
for i in inp:
    if(i[0] == 'E'):
        q.enQueue(i[2])
        print(q.lst2Q(", "))
    elif(i[0] == 'D' and not q.isEmpty()):
        temp = q.deQueue()
        print(f'{temp} <- {q.lst2Q(", ")}')
        dq.enQueue(temp)
    elif q.isEmpty():
        print("Empty")
print(f'{dq.lst2Q(", ")} : {q.lst2Q(", ")}')



    
