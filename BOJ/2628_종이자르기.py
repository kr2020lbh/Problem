import sys
sys.stdin = open("input.txt","r")
c,r = map(int,input().split())
res = [[r],[c]]
for i in range(int(input())):
    direction, cut = map(int,input().split())

    tmp = []
    SUM = 0
    for i in range(len(res[direction])):

        if cut < SUM+res[direction][i]:
            tmp.append(cut-SUM)
            tmp.append(res[direction][i] - (cut-SUM))
            break
        else: tmp.append(res[direction][i])

        SUM += res[direction][i]
    tmp += res[direction][i+1::]
    res[direction] = tmp[::]


MAX = 0
for r in res[0]:
    for c in res[1]:
        if MAX < r*c:
            MAX = r*c
print(MAX)