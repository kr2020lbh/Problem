#[S/W 문제해결 응용] 7일차 - 행렬찾기

import sys
sys.stdin = open("input.txt","r")
def bfs():
    global n
    M=N=1
    while queue:
        x,y = queue.pop(0)
        for a,b in move:
            d_x = x+a
            d_y = y+b

            if (d_x<n) and (d_y<n) and arr[d_x][d_y]!=0:
                M+=a
                N+=b
                queue.append((d_x,d_y))
    return M,N

def array_to_zero(i,j,m,n):
    for a in range(m):
        for b in range(n):
            arr[i+a][j+b]=0

move = [(1,0),(0,1)]

for t in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    arr_sizes=[]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j]!=0:
                queue = [(i,j)]
                a,b = bfs()
                print(t, i, j, a, b)
                array_to_zero(i,j,a,b)

                arr_sizes.append([a*b,a,b])

    # result = ''
    # for size in array_size:
    #     result+=str(size[0])+' ' + str(size[1])+' '
    # print(f'#{t} {len(array_size)} {result}')