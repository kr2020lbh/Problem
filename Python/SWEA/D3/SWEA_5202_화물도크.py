import sys
sys.stdin = open("input.txt", "r")




for t in range(1,int(input())+1):
    N = int(input())
    times = [[] for _ in range(25)]
    res = 0
    for _ in range(N):
        s,e = map(int,input().split())
        times[e].append(s)

    idx = 24
    while True:
        tmp = []
        for i in range(idx,-1,-1):
            tmp.extend(times[i])
        if tmp:
            idx = max(tmp)
            res += 1
        else:
            break

    print("#{} {}".format(t,res))

