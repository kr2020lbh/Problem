import sys
sys.stdin = open("input.txt","r")
def f(idx):

    if idx==M:
        result = ' '.join(map(str,ptr))
        print(result)

    else:
        prev_pivot = 0

        for i in range(N):

            if visited[i] == 1:
                continue
            if prev_pivot == arr[i]:
                continue
            visited[i] = 1
            prev_pivot = arr[i]
            ptr.append(arr[i])
            f(idx+1)
            visited[i] = 0
            ptr.pop()


N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visited = [0]*N
prev = 0
ptr = []
f(0)