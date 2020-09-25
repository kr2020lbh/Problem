#1493. 수의 새로운 연산
import sys
import pprint
sys.stdin = open("input.txt","r")

def find_xy(p,arr):
    for i,ar in enumerate(arr):
        if p in ar:
            y = i+1
            for j,a in enumerate(ar):
                if p == a:
                    x = j+1
                    return x,y

arr = [[0]*500 for _ in range(500)]
val = 1
row = col = 0
for i in range(len(arr)*(len(arr)+1)//2):
    arr[row][col] = val
    d_row = row-1
    d_col = col+1
    if d_row < 0:
        row = col+1
        col = 0
    else:
        row = d_row
        col += 1
    val+=1

result = []
for t in range(1,int(input())+1):
    p,q = map(int,input().split())
    i = find_xy(p,arr)[1]+find_xy(q,arr)[1]-1
    j = find_xy(p,arr)[0]+find_xy(q,arr)[0]-1
    result.append(f'#{t} {arr[i][j]}')
for ans in result:
    print(ans)