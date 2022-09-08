class Queue:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self,ele):
        return self.items.append(ele)

    def deQueue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        
    def isEmpty(self):
        return self.items == []
    
    def __str__(self):
        return str(self.items)

q1 = Queue([1,2,3])
q2 = Queue()
q2.enQueue(q1.deQueue())
print(q2)
