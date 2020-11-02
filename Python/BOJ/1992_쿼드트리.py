import sys
sys.stdin = open("input.txt","r")
def is_same(row,col,n):
    start = arr[row][col]
    for i in range(row,row+n):
        for j in range(col,col+n):
            if start != arr[i][j]:
                return False
    return True

def solution(row,col,N):
    print('(',end='')
    #왼쪽위
    if is_same(row,col,N//2):
        print(arr[row][col],end='')
    else:
        solution(row,col,N//2)
    #오른쪽위
    if is_same(row,col+N//2,N//2):
        print(arr[row][col+N//2],end='')
    else:
        solution(row,col+N//2,N//2)
    #왼쪽아래
    if is_same(row+N//2,col,N//2):
        print(arr[row+N//2][col],end='')
    else:
        solution(row+N//2,col,N//2)
    #오른쪽아래
    if is_same(row+N//2,col+N//2,N//2):
        print(arr[row+N//2][col+N//2],end='')
    else:
        solution(row+N//2,col+N//2,N//2)
    print(')',end='')

N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
if is_same(0,0,N):
    print(arr[0][0])
else:
    solution(0,0,N)