num=int(input("Enter Input : "))

for i in range(num+2):
    for j in range(num-i+1):
        print('.',end='')
    for j in range(i+1):
        print('#',end='')
    for j in range(num+2):
        if i==0 or i==num+1:
            print('+',end='')
        elif j!=0 and j!=num+1:
            print('#',end='')
        else:
            print('+',end='')
    print('')

for i in range(num+2):
    for j in range(num+2):
        if i==0 or i==num+1:
            print('#',end='')
        elif j!=0 and j!=num+1:
            print('+',end='')
        else:
            print('#',end='')
    for j in range(num-i+2):
        print('+',end='')
    for j in range(i):
        print('.',end='')
    print('')
# rows = int(input("Enter Input : "))
# # count = 2*n+4;

# for i in range(0, rows):
#     for j in range(rows - 1, i, -1):
#         print(j, '', end='')
#     for l in range(i):
#         print('    ', end='')
#     for k in range(i + 1, rows):
#         print(k, '', end='')
#     print('\n')