import sys
sys.stdin = open("input.txt", "r")

d_row = [1,0]
d_col = [0,1]

def visit(cur,logs,total):
    global MIN
    if total > MIN:return
    row, col = cur
    if N-1 == cur[0] and N-1 == cur[1]:
        if total < MIN:
            MIN = total

    else:
        for i in range(2):
            dr = row + d_row[i]
            dc = col + d_col[i]
            if dr < N and dc < N:
                visit([dr,dc],logs+[cur],total+arr[dr][dc])




for t in range(int(input())):
    N = int(input())
    MIN = 100000
    arr = [list(map(int,input().split())) for _ in range(N)]
    visit([0,0,],[],arr[0][0])
    print("#{} {}".format(t+1,MIN))

