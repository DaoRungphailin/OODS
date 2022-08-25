class Stack:
    def __init__(self, max=None, park=None) -> None:
        if list is None:
            self.items = []
        else:
            self.items = park
        self.limit = max
    
    def __str__(self):
        return str(self.items)

    def __getitem__(self, i:int):
        return self.items[i]

    def __len__(self):
        return len(self.items)
        
    def push(self,str):
        if not self.isFull(): 
            self.items.append(str)
        
    def pop(self, index=-1):
        if not self.isEmpty():
            return self.items.pop(index)
        else:
            print("Stack is Empty.")
    
    def isEmpty(self):
        return self.__len__() == 0
    
    def isFull(self):
        return self.__len__() == self.limit

class Soi(Stack):
    def __init__(self, max, park, operation, car):
        super(Soi, self).__init__(max=max, park=park)
        self.operation = operation
        self.car = car 

    def checkCar(self, x):
        for car in self.items:
            if car == x:
                return True
        return False

    def arrive(self, x):
        if self.isFull():
            print(f'cannot {self.operation} : Soi Full')
        elif self.checkCar(x):
            print(f'already in soi')
        else:
            self.push(x)
            print(f'arrive! : Add Car {self.car}')

    def depart(self, x):
        if self.isEmpty():
            print(f'cannot depart : Soi Empty')
        elif not self.checkCar(x):
            print(f'cannot depart : Dont Have Car {self.car}')
        else:
            self.pop(0)
            print(f'depart ! : Car {self.car} was remove')

    def solve(self):
        if self.items[0] == 0:
            self.pop()
        print(f'car {self.car} ', end='')
        if self.operation == 'depart':
            self.depart(self.car)
        if self.operation == 'arrive':
            self.arrive(self.car)
        print(self.__str__())

print("******** Parking Lot ********")
max,park,operation,car = input("Enter max of car,car in soi,operation : ").split()
park = park.split(',')
park = list(map(int , park))
s = Soi(int(max),park,operation,int(car))
s.solve()


