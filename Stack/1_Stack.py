class Stack():
    def __init__(self):
        self.items = []
        self.size = len(self.items)
        
    def push(self,num):
        self.items.append(int(num))
        self.size += 1
        self.items.sort()
        return f'Add = {num} and Size = {self.size}'
    
    def pop(self):
        if self.items == []:
            print("-1")
            return -1
        else:
            self.size -= 1
            print(f"Pop = {self.items[-1]} and Index = {self.size}")
            self.items.pop()

enter = input("Enter Input : ").split(",")
stack = Stack()

for i in range(len(enter)):
    try:
        key, number = enter[i].split()
    except:
        key = enter[i][0]
    if key == 'A':
        print(stack.push(number))
    elif key == 'P':
        stack.pop()
if stack.items == []:
    print("Value in Stack = Empty")
else:
    print("Value in Stack =",*stack.items)