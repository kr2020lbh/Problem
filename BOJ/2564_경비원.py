import sys
sys.stdin = open("input.txt","r")

row,col = map(int,input().split())
n = int(input())
arr = []

for i in range(n+1):
    direct,howfar = map(int,input().split())
    arr.append([direct,howfar])
me = arr[-1]
res = 0
if me[0] == 1: #북
    for i in range(n):
        store = arr[i]
        if store[0]==me[0]: #북,북
            res+=abs(store[1]-me[1])
        elif store[0] == 2: #북,남
            res+=col+min((store[1]+me[1]),(row-store[1]+row-me[1]))
        elif store[0] == 3: #북,서
            res+=store[1]+me[1]
        elif store[0] == 4: #북,동
            res+=store[1]+row-me[1]
elif me[0] == 2: #남
    for i in range(n):
        store = arr[i]
        if store[0]==me[0]: #남,남
            res+=abs(store[1]-me[1])
        elif store[0] == 1: #남,북
            res+=col+min((store[1]+me[1]),(row-store[1]+row-me[1]))
        elif store[0] == 3: #남,서
            res+=col-store[1]+me[1]
        elif store[0] == 4: #남,동
            res+=col-store[1]+row-me[1]
elif me[0] == 3: #서
    for i in range(n):
        store = arr[i]
        if store[0]==me[0]: #서,서
            res+=abs(store[1]-me[1])
        elif store[0] == 1: #서,북
            res+=me[1]+store[1]
        elif store[0] == 2: #서,남
            res+=col-store[1]+me[1]
        elif store[0] == 4: #서,동
            res+=row + min((store[1]+me[1]),(col-store[1]+col-me[1]))
elif me[0] == 4: #동
    for i in range(n):
        store = arr[i]
        if store[0]==me[0]: #동,동
            res+=abs(store[1]-me[1])
        elif store[0] == 2: #동,남
            res+=col-me[1] + row -store[1]
        elif store[0] == 3: #동,서
            res+=row + min((me[1]+store[1]),(col-me[1]+col-store[1]))
        elif store[0] == 1: #동,북
            res+= row - store[1] + me[1]
print(res)