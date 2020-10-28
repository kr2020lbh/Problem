import sys
sys.stdin = open("input.txt", "r")

def check(start_point,k):
    row,col = start_point
    if k == 1:
        answer[arr[row][col]] += 1
    else:
        flag = True
        element = arr[row][col]
        for i in range(k):
            if arr[row+i][col:col+k].count(element) != k:
                flag = False
                break
        if flag:
            answer[arr[row][col]] += 1
        else:
            for i in range(0,k,k//3):
                for j in range(0,k,k//3):
                    check([row+i,col+j],k//3)


n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
answer = [0,0,0]
check([0,0],n)
answer = [answer[-1],answer[0],answer[1]]
[print(a) for a in answer]