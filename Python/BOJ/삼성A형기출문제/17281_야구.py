import sys

sys.stdin = open("input.txt","r")

from itertools import permutations
#반복문으로 할당하기엔 시간 초과가 난다..
def get_score(score,start,order):
    out=b1=b2=b3=res = 0
    while out<3:
        tmp = score[order[start]-1]
        if tmp == 0:
            out+=1
        elif tmp==1:
            res+=b3
            b1,b2,b3 = 1,b1,b2
        elif tmp==2:
            res+=(b3+b2)
            b1,b2,b3 = 0,1,b1
        elif tmp==3:
            res+=(b3+b2+b1)
            b1,b2,b3 = 0,0,1
        elif tmp==4:
            res += (b3 + b2 + b1 + 1)
            b1, b2, b3 = 0, 0, 0

        start=(start+1)%9

    return res,start


n = int(input())
scores = [list(map(int,input().split())) for _ in range(n)]

MAX = 0
for perm in permutations(range(2,10),8):
    perm = list(perm[0:3]) + [1] + list(perm[3:])
    start = 0
    res = 0
    for score in scores:
        res_tmp,start = get_score(score,start,perm)
        res+=res_tmp
    if res > MAX:MAX = res
print(MAX)
