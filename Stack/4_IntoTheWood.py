class Stack:

    def __init__(self, list1=[]):
        if list1 == None:
            self.items = []
        else:
            self.items = list1
        self.size = len(self.items)

    def push(self, str):
        self.items.append(str)
        self.size += 1
        return str

    def pop(self):
        if self.items == []:
            return -1
        else:
            self.size -= 1
            return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []

    def __str__(self):
        return str(self.items)


def CheckTallest(n):
    i = 1
    st = Stack([S.peek()])
    stc = Stack([])

    while (not S.isEmpty()):
        if (int(n) < int(S.peek())): #check near tree < next tree
            i += 1 #see
            n = S.peek()
            st.push(S.peek())
        S.pop()
    while (not st.isEmpty()):
        stc.push(st.pop())

    return i, stc


S = Stack()
enter = input('Enter Input : ').split(',')
for i in range(len(enter)):
    try:
        key, number = enter[i].split()
    except:
        key = enter[i][0]
    if key == 'A':
        S.push(number)
    elif key == 'B':
        if (S.isEmpty()):
            print(0)
        else:
            n, S = CheckTallest(S.peek())
            print(n)
