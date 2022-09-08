from operator import truediv


class Stack():
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []
        
    def push(self,ele):
        return self.items.append(ele)

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print('Stack is Empty. Cannot peek!!')

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def __str__(self):
        return str(self.items)

def match(open,close):
    if open == '(' and close == ')':
        return True
    if open == '{' and close == '}':
        return True
    if open == '[' and close == ']':
        return True

inp = input('Enter Input : ')
error = 0
countOpen = 0
countClose = 0
stack = Stack()
for i in inp:
    if i in '([{':
        stack.push(i)
    elif i in ')]}':
        if stack.isEmpty():
            stack.push(i)
            error = 3 #close excess
        elif not match(stack.peek(),i):
            error = 1 #UNMATCH
        elif match(stack.peek(),i):
            stack.pop()
            if stack.isEmpty():
                error = 2 #MATCH
            
if not stack.isEmpty():
    for j in stack.items:
        if j in '([{':
            countOpen += 1
        elif j in ')]}':
            countClose += 1

if error == 1 :
    print('Unmatch')
elif error == 2:
    print('MATCH')
elif countOpen != 0:
    print(f'Open excess {countOpen}')
elif countClose != 0 and error == 3:
    print(f'Close excess {countClose}')



