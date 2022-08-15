n = int(input("Enter Input : "))
count = 2*n+4;
for i in range(1,count):
    for j in range(1,count):
        if (j > i or j < count): 
            print(".",end="")
        else:
            print("#",end="")
    print()
print()