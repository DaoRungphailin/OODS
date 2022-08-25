class Stack():
    def __init__(self):
        self.items = []
        self.size = len(self.items)
        
    def push(self,str):
        self.items.append(str)
        self.size += 1
        self.items.sort()
        return str
    
    def pop(self):
        if self.items == []:
            return -1
        else:
            self.size -= 1
            return self.items.pop()

def match(open,close):
    opens = "{[("
    closes = "}])"
    return opens.index(open) == closes.index(close) 

    # return (open == '(' and close == ')') or \
    #     (open == '{' and close == '}') or \
    #         (open == '[' and close == ']')

def parenMatching(str):
    s = Stack()
    i= 0
    error = 0
    while i< len(str) and error == 0 :
        c = str[i]
        if c in '{[(':
            s.push(c)
        else:
            if c in '}])':
                if s.size > 0:
                    if not match(s.pop(),c):
                        error = 1 #NOT MATCH มันโดนทับ
                else:
                    error = 2 #close paren excess
        i += 1
    if s.size > 0 and error == 0:
        error = 3 #open paren(s) excess
    return error,c,i,s

stack = Stack()
stack = str(input("Enter expresion : "))

err,c,i,s = parenMatching(stack)   
if err == 1:
    print(stack, 'Unmatch open-close')
elif err == 2:
    print(stack, 'close paren excess')
elif err == 3:
    print(stack, 'open paren excess  ', s.size,': ',end='') 
    for ele in s.items:
        print(ele,sep=' ',end = '')
    print()
else: 
    print(stack, 'MATCH')