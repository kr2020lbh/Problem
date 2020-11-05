answer = []

def dfs(idx,visited,N,tickets,order):
    if sum(list(map(int,bin(visited)[2::]))) == N:
        res = []
        for i in range(N):
            res.append(tickets[order[i]][0])
            if i == N-1:
                res.append(tickets[order[i]][1])
        answer.append(res)

    for i in range(N):
        if not(visited & (1<<i)) and tickets[idx][1] == tickets[i][0]:
            dfs(i,visited | (1<<i),N,tickets,order+[i])


def solution(tickets):
    N = len(tickets)

    for i in range(N):
        if tickets[i][0] == 'ICN':
            dfs(i,1<<i,N,tickets,[i])
    return sorted(answer)[0]


# solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])