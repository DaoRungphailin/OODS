class Queue():
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self, ele):
        return self.items.append(ele)

    def __str__(self):
        return str(self.items)


inp = input('Enter code,hint : ').split(',')
q = Queue()
lst = []
lst.extend(inp[0])
i = 0
for i in range(len(lst)):
    change = ord(lst[0]) - ord(inp[1])
    ans = (ord(lst[i]) - change)
    q.enQueue(chr(ans))
    print(q)
