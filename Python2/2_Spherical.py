import math
class Spherical:
    def __init__(self,r):
        self.radius = r

    def changeR(self,Radius):
        self.radius = Radius

    def findVolume(self):
        print("Volume = ",self.radius**3*math.pi)

    def findArea(self):
        print("Area = ",self.radius**2*math.pi)

#print("<class '__main__.Spherical'>")
#print("['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'changeR', 'findArea', 'findVolume', 'radius']")
r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(R1.findVolume)
