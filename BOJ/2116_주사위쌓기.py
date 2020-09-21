import sys
sys.stdin = open("input.txt","r")


def find_MAX(index,dices):
    tmp = 0
    for t in range(6):
        if t in index:
            continue
        if dices[t] > tmp:
            tmp = dices[t]
    return tmp


indexes = [[0,5],[1,3],[2,4],[3,1],[4,2],[5,0]]
n = int(input())
dices = []
for i in range(n):
    dices.append(list(map(int,input().split())))

MAX = 0
for i in range(6):
    start = dices[0][i]
    SUM =find_MAX(indexes[i],dices[0])
    for j in range(1,n):
        for k in range(6):
            if dices[j][k] == start:
                start = dices[j][indexes[k][1]]
                SUM+=find_MAX(indexes[k],dices[j])
                break
    if MAX < SUM :
        MAX = SUM
print(MAX)