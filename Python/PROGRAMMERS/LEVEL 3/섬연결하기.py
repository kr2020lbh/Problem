def findset(p,x):
    while x != p[x]:
        x = p[x]
    return x

def unionset(p,x,y):
    p[findset(p,y)] = findset(p,x)
    return p


def solution(n, costs):
    p = [i for i in range(n)]
    costs.sort(key=lambda x:x[-1])
    answer = 0

    for x,y,cost in costs:
        if findset(p,x) != findset(p,y):
            unionset(p,x,y)
            answer += cost
    return answer



costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
n = 4
solution(n,costs)