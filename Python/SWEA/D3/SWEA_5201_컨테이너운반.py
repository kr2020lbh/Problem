import sys
sys.stdin = open("input.txt", "r")
for t in range(1,int(input())+1):
    N,M = map(int,input().split())
    weight_visit = [0]*N
    truck_visit = [0]*M
    weights = sorted(list(map(int,input().split())),reverse=True)
    trucks = sorted(list(map(int,input().split())),reverse=True)
    res = 0
    for i in range(N):
        for j in range(M):
            if truck_visit[j] == 0 and weight_visit[i]==0:
                if trucks[j] >= weights[i]:
                    res += weights[i]
                    truck_visit[j] = 1
                    weight_visit[i] = 1

    print("#{} {}".format(t,res))