class funString():

    def _size_(self,str) :
        self.str = str
        print(len(str))

    def changeSize(self):
        print(str.capitalize())

    def reverse(self):
        print("")

    def deleteSame(self):
        print("")


str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())