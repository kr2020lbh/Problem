import sys
sys.stdin = open("input.txt","r")

N = input()
under_limit = int(N)-len(N)*9 if int(N)>18 else 0

for i in range(under_limit,int(N)):
    constructor = int(i)
    for j in str(i):
        constructor+=int(j)
    if constructor==int(N):
        print(int(i))
        break
else:
    print(0)
