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

    def peek(self):
        return self.items[-1]

    def __str__(self):
        return str(self.items)

Operators = {'+', '-', '*', '/', '(', ')', '^'} 
Priority = {'+':1, '-':1, '*':2, '/':2, '^':3}

def InfixToPosfix(str):
    s = Stack()
    output = ''
    i=0
    while i< len(str):
        c = str[i]
        if s.size >= 0:
            if c.isalpha():
                output += c
            else:
                s.push(c)
                #print(s.peek())
                if Priority[s.peek()] > Priority[c]: #check pruority if small push if big pop
                    print("check")
                    output += s.pop()
        i+=1
    print("output = " ,output)
    print("Operator = " ,s)


infix = input("Enter Infix : ")
InfixToPosfix(infix)