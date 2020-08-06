import sys
sys.stdin = open("input.txt", "r")
def osello_reset(arr):
    center = len(arr)//2
    arr[center - 1][center - 1] = 1
    arr[center][center] = 1
    arr[center - 1][center] = 2
    arr[center][center - 1] = 2
    return

def check_between_row(arr,pivot_row,pivot_col,check_col,stone):
    if stone == 1:
        another_stone = 2
    else:
        another_stone = 1
    if pivot_col > check_col:
        for j in range(check_col+1,pivot_col):
            if arr[pivot_row][j]==another_stone:
                pass
            else:
                return
        else:
            arr[pivot_row][check_col:pivot_col]=[stone]*(pivot_col-check_col)
    elif pivot_col < check_col:
        for j in range(pivot_col+1,check_col):
            if arr[pivot_row][j]==another_stone:
                pass
            else:
                return
        else:
            arr[pivot_row][pivot_col+1:check_col] = [stone] * (check_col - pivot_col-1)

def check_between_col(arr,pivot_row,pivot_col,check_row,stone):
    if stone == 1:
        another_stone = 2
    else:
        another_stone = 1
    if pivot_row > check_row:
        for j in range(check_row+1,pivot_row):
            if arr[j][pivot_col]==another_stone:
                pass
            else:
                return
        else:
            arr[check_row:pivot_row][pivot_col]=[stone]*(pivot_row-check_row)
    elif pivot_row < check_row:
        for j in range(pivot_row+1,check_row):
            if arr[j][pivot_col]==another_stone:
                pass
            else:
                return
        else:
            arr[pivot_row+1:check_row][pivot_col] = [stone] * (check_row - pivot_row-1)





for t in range(1,int(input())+1):
    N,M=map(int,input().split())
    arr=[[0]*N for _ in range(N)]
    osello_reset(arr)
    for _ in range(M):
        y,x,stone = map(int,input().split())
        i = y-1
        j = x-1
        for k in range(len(arr)):
            check_between_row(arr,i,j,k,stone)
            check_between_col(arr, i, j, k, stone)
    print(arr)



