import sys
sys.stdin = open("input.txt","r")
col,row = map(int,input().split())
n = int(input())
d_r = [-1,0,1,0]
d_c = [0,1,0,-1]

arr = [[1]+[0]*col+[1] for _ in range(row+2)]
arr[0],arr[-1] = [1]*(col+2), [1]*(col+2)


r,c=row,1

cnt = 1

mode = 0

if n < row*col+1:
    while cnt <= row * col:
        if cnt == n:
            print(c, row - (r - 1))
            break
        arr[r][c] = cnt

        if arr[r + d_r[mode]][c + d_c[mode]] != 0:
            mode += 1
            mode %= 4
        r, c = r + d_r[mode], c + d_c[mode]
        cnt += 1

else:
    print(0)

