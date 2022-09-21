def GCD(A, B):
    if B == 0:
        return abs(A)
    else:
        return GCD(B, A % B)


A, B = list(map(int, input('Enter Input : ').split(' ')))
if B > A:
    temp = B
    B = A
    A = temp
    
if A == 0 and B == 0:
    print('Error! must be not all zero.')
else:
    print(f'The gcd of {A} and {B} is : {GCD(A,B)}')
