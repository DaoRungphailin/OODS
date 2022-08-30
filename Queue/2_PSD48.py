class Queue():
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self, ele):
        self.items.append(ele)

    def deQueue(self):
        if not self.isEmpty():
            return self.items.pop(0)

    def insert(self, index, ele):
        return self.items.insert(index, ele)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def lst2Q(self):
        return 'Empty' if self.isEmpty() else '\n'.join(self.items)

inp = list(input("Enter Input : ").split(','))
q = Queue()
dq = Queue()
ES = 0
for i in range(len(inp)):
    try:
        key, number = inp[i].split()
    except:
        key = inp[i][0]
    if key == 'EN':
        q.enQueue(number)
    elif key == 'ES':
        q.insert(ES,number)
        ES += 1
    elif key == 'D' :
        if q.size() > 0: 
            if(ES > 0):
                ES -= 1
            print(q.deQueue()) 
        elif q.isEmpty():
            print('Empty')
