#건초더미
import sys
sys.stdin = open("input.txt","r")
for t in range(1,int(input())+1):
    N = int(input())
    hay = []
    for i in range(N):
        hay.append(int(input()))

    same = sum(hay)//N
    cnt=0
    for i in range(N):
        cnt+=abs(hay[i]-same)
    print('#{} {}'.format(t,cnt//2))
