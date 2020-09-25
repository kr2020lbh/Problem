import sys
sys.stdin = open("input.txt","r")

def check_bingo_row_and_col(arr1,arr2):
    cnt=0
    for i in range(5):
        if sum(arr1[i])==0:
            cnt+=1
        if sum(arr2[i])==0:
            cnt+=1
    return cnt


def check_bingo_diagonal(arr1):
    cnt=0
    for i in range(5):
        if arr1[i][i]!=0:
            break
    else:cnt+=1

    for i in range(5):
        if arr1[i][4-i]!=0:
            break
    else:cnt+=1

    return cnt


def num_to_zero(num):
    for i in range(5):
        for j in range(5):
            if arr1[i][j] == num:
                arr1[i][j] = 0
                return


def is_bingo(arr1,ans):
    for i in range(5):
        for j in range(5):
            num_to_zero(ans[i][j])
            if check_bingo_row_and_col(arr1, list(map(list, zip(*arr1)))) + check_bingo_diagonal(arr1) >= 3:
                return i * 5 + j + 1



arr1= [list(map(int,input().split())) for _ in range(5)]
ans = [list(map(int,input().split())) for _ in range(5)]
print(is_bingo(arr1,ans))


