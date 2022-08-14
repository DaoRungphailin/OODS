def mod_position(arr, s):
    ans = []
    for i in range(len(arr)):
        if (i+1) % s == 0:
            ans.append(arr[i])
    print(ans)

print("*** Mod Position ***")
string, n = input("Enter Input : ").split(",")
mod_position(string,int(n))