#2806. N-Queen
import sys
sys.stdin = open("input.txt","r")
import pprint
def queen(arr,i,j,n):
    #상하좌우
    for x in range(n):
        if x!=j:
            arr[i][x] = 0
        if x!=i:
            arr[x][j] = 0
    left_up=left_down=right_up=right_down = True
    for k in range(1,n):
        if i-k<0 or j-k<0:
            left_up = False
        if i+k>n-1 or j-k<0:
            left_down = False
        if i-k<0 or j+k>n-1:
            right_up = False
        if i+k>n-1 or j+k >n-1:
            right_down = False
        if left_up:
            arr[i-k][j-k]=0
        if left_down:
            arr[i+k][j-k]=0
        if right_up:
            arr[i-k][j+k]=0
        if right_down:
            arr[i+k][j+k]=0

for t in range(1,int(input())+1):
    N = int(input())
    count = 0
    arr = [[1]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j]==1:
                queen(arr,i,j,N)
    pprint.pprint(arr)



