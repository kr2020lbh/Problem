import sys
sys.stdin = open("input.txt","r")

arr = [[0]*101 for _ in range(101)]
t = int(input())
papers = [0]*(t+1)
for n in range(1,t+1):
    x,y,w,h = map(int,input().split())
    for i in range(x,x+w):
        for j in range(y,y+h):
            if arr[i][j]!=0:
                papers[arr[i][j]] -= 1
            papers[n] += 1
            arr[i][j] = n
[print(paper) for paper in papers[1::]]

