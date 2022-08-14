print("*** Fun with Drawing ***")
num = int(input("Enter input : "))
count = 4*num -3 
for i in range(1, count+1):
    for j in range(1, count+1):
        if (j < i or j > count-i+1) and not(j <= i and j >= count-i+1): 
            if j % 2 == 0 :
                print(".", end="")
            else :
                print("#", end="")
        else:
            if i % 2 == 0 :
                print(".", end="")
            else :
                print("#", end="")
    print()
