import sys
sys.setrecursionlimit(10**8)

def dfs(idx,a,arr,visited):
    global answer
    visited[idx] = 1
    for i in arr[idx]:
        if not visited[i]:
            a[idx] += dfs(i,a,arr,visited)
    answer += abs(a[idx])
    return a[idx]

def solution(a, edges):
    global answer
    answer = 0

    if sum(a) != 0:
        return -1

    lenA = len(a)
    arr = [[] for _ in range(lenA)]

    for i,j in edges:
        arr[i].append(j)
        arr[j].append(i)

    visited = [0] * lenA
    dfs(0, a, arr, visited)
    return answer



solution([-5,0,2,1,2]	,[[0,1],[3,4],[2,3],[0,3]]	)