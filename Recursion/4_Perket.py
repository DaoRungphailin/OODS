listPerket = []

def perket(index,n,s,b):
    
    if(index==len(lst)):
        if(n != 0):
            ans= abs(s-b)
            listPerket.append(ans)
    else:
        tempS , tempB = map(int,lst[index].split(' '))
        #Recursive
        perket(index + 1, n, s, b)
        perket(index + 1, n + 1, s*tempS,b+tempB)



lst = list(map(str,input("Enter Input : ").split(',')))
perket(0,0,1,0)
print(min(listPerket))
