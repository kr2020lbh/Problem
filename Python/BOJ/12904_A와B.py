import sys
sys.stdin = open("input.txt","r")

S = input()
T = input()
L = len(T) - len(S)

for i in range(L):
    if T[-1] == 'A':
        T = T[0:len(T)-1]
    else:
        T = T[0:len(T)-1]
        T = T[::-1]
if S == T:
    print(1)
else:
    print(0)
