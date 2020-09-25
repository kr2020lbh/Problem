import sys
sys.stdin = open("input.txt","r")

arr = [[0]*101 for _ in range(101)]
for _ in range(int(input())):
    x,y = map(int,input().split())
    for i in range(10):
        arr[x+i][y:y+10] = [1]*10
cnt=0
for a in arr:
    cnt+=a.count(1)
print(cnt)