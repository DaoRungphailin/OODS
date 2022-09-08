class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        s = 'Value in Stack = '
        if self.isEmpty():
            s += 'Empty'
        else:
            for ele in self.items:
                s += str(ele) + ' '
        return s

def isRepeat(i):
    if S.isEmpty() or S.peek() != i:
        return False
    elif S.size() > 1:
        bin = S.pop()
        if S.peek() == i:
            S.pop()
            return True
        else:
            S.push(bin)
            return False

inp = input('Enter Input : ').split()
S = Stack()
cnt = 0

for i in inp:
    if not isRepeat(i):
        S.push(i)
    else:
        cnt += 1

print(S.size())

if S.isEmpty():
    print('Empty',end='')
else:
    for j in range(S.size()):
        print(S.pop(), end='')
print()

if cnt > 1:
    print('Combo : ' + str(cnt) + ' ! ! !')



# def isRepeat():
#     if S.isEmpty() or S.peek() != inp.peek():
#         return False
#     elif S.size() > 1:
#         bin = S.pop()
#         if S.peek() == inp.peek():
#             S.pop()
#             return True
#         else:
#             S.push(bin)
#             return False

# inp = Stack(input('Enter Input : ').split())
# S = Stack()
# cnt = 0

# while not inp.isEmpty():
#     if not isRepeat():
#         S.push(inp.pop())
#     else:
#         inp.pop()
#         cnt += 1

# print(S.size())

# while not S.isEmpty():
#     inp.push(S.pop())

# if inp.isEmpty():
#     print('Empty',end='')
# else:
#     while not inp.isEmpty():
#         print(inp.pop(),end='')

# if cnt > 1:
#     print('\nCombo : ' + str(cnt) + ' ! ! !')