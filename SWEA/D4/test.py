
N = int(input())
if N%2:
    A = N%2+N//2
    B = N-A
else:A=B=N//2
for _ in range(N):
    for i in range(A):print('*',end=' ')
    else:print()
    for i in range(B):print(' ',end='*')
    else:print()
