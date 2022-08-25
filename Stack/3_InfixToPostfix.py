from ast import operator
class Stack():
    def __init__(self):
        self.items = []
        self.size = len(self.items)
        
    def push(self,str):
        self.items.append(str)
        self.size += 1
        return str
    
    def pop(self):
        if self.items == []:
            return -1
        else:
            self.size -= 1
            return self.items.pop()

    def peek(self,n):
        return self.items[-n]

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
            elif(s.size == 0):
                s.push(c)
            elif(c == ')'):
                while(c != '('):
                    output += s.pop()
                    i+=1
                    c = str[i]

            else:
                print(s)
                if(s.size > 1):
                    print(f's.peak1 = {s.peek(1)}, s.peak2 = {s.peek(2)}')
                    print(f's.peak1 = {Priority[s.peek(1)]}, s.peak2 = {Priority[s.peek(1)]}')
                if(s.size > 1 and Priority[s.peek(1)] > Priority[s.peek(2)]):#check pruority if small push if big pop
                    print("check")
                    output += s.pop()
                    output += s.pop()
                elif(s.size > 1 and Priority[s.peek(1)] < Priority[s.peek(2)]):
                    s.push(c)

        i+=1
    while(s.size != 0):
        output += s.pop()
    print("output = " ,output,type(output))
    print("Operator = " ,s,type(operator))

infix = input("Enter Infix : ")
InfixToPosfix(infix)