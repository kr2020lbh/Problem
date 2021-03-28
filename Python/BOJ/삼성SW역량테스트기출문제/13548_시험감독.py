import sys
sys.stdin = open("input.txt","r")

N = int(input())
rooms = list(map(int,input().split()))
main,sub = map(int,input().split())
ans = 0
for i in range(N):
    room = rooms[i]
    remain = room - main
    if remain > 0:
        if remain // sub:
            if remain % sub:
                ans = ans + 2 + (remain) // sub
            else:
                ans = ans + 1 + (remain) // sub
        else:
            ans = ans + 2
    else:
        ans += 1
print(ans)