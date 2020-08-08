#스도쿠 검증
import sys
sys.stdin = open("input.txt","r")
def get_square(arr,i,j):
    square = []
    for i in range(3):
        square.extend(arr[i][j:j+3])
    return square

def get_col(arr,i):
    col = []
    for j in range(9):
        col.append(arr[j][i])
    return col

for t in range(1,int(input())+1):
    arr=[list(map(int,input().split())) for _ in range(9)]

    for i in range(9):
        if(sum(arr[i])!=45 or sum(get_col(arr,i))!=45):
            sudoku=0
            break
    else: sudoku=1

    if sudoku==1:
        for i in range(0,7,3):
            for j in range(0,7,3):
                if sum(get_square(arr, i, j)) != 45:
                    sudoku = 0

    print(f'#{t} {sudoku}')