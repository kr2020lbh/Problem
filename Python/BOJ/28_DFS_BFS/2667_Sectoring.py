import sys
sys.stdin = open("input.txt","r")
# row,col, [1][1] 부터 [N][N] 까지 돌아본다.
# 그때 0이 아닌 수가 나오면 주변을 탐색한다.
# 탐색하면서 1을 0으로 바꿔준다.
# cnt 한다.
def sectoring(row,col):
    sector[row][col] = 0
    cnts[-1] +=1
    if sector[row - 1][col] != 0: sectoring(row-1,col)
    if sector[row + 1][col] != 0: sectoring(row+1,col)
    if sector[row][col - 1] != 0: sectoring(row,col-1)
    if sector[row][col + 1] != 0: sectoring(row,col+1)

N = int(input())
sector = [0] * (N+2)
sector[0] = [0]*(N+2)
sector[-1] = [0]*(N+2)
cnts = []
for i in range(1,N+1):
    sector[i] = [0] + list(map(int,input())) + [0]
for row in range(1,N+1):
    for col in range(1,N+1):
        if sector[row][col] != 0:
            cnts.append(0)
            sectoring(row,col)
cnts.sort()
print(len(cnts))
for i in range(len(cnts)):
    print(cnts[i])

