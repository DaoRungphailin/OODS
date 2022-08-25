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

    def peek(self):
        return self.items[-1]

    def __str__(self):
        return str(self.items)

Operators = set(['+', '-', '*', '/', '(', ')', '^'])  # collection of Operators

Priority = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities of Operators
 
def infixToPostfix(expression): 

    stack = Stack() # initialization of empty stack

    output = '' 

    

    for character in expression:

        if character not in Operators:  # if an operand append in postfix expression

            output+= character

        elif character=='(':  # else Operators push onto stack

            stack.push('(')

        elif character==')':

            while stack.size != 0  and stack.peek()!= '(':

                output+=stack.pop()

            stack.pop()

        else: 

            while stack.size != 0  and stack.peek() != '(' and Priority[character]<=Priority[stack.peek()]:

                output+=stack.pop()

            stack.push(character)

    while stack.size != 0 :

        output+=stack.pop()

    return output


expression = input('Enter Infix : ')
print('Postfix :',infixToPostfix(expression))