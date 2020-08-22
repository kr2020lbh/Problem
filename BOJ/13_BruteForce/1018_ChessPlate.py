import sys
sys.stdin = open("input.txt","r")

def compare_row(row,k):
    for i in range(8):
        if row[i]!=chess1[k][i]:
            result[0]+=1
        else:
            result[1]+=1
    return
N,M = map(int,input().split())
chess = [ input() for _ in range(N) ]
chess1 = []
chess2 = []

row1 = 'BW'*4
row2 = 'WB'*4

for i in range(8):
    if i%2==0:
        chess1.append(row1)
        chess2.append(row2)
    else:
        chess1.append(row2)
        chess2.append(row1)

MIN = 64
for i in range(N-8+1):
    for j in range(M-8+1):
        result = [0, 0]
        for k in range(8):
            compare_row(chess[i+k][j:j+8],k)
        if MIN > min(result[0],result[1]):
            MIN = min(result[0],result[1])
print(MIN)