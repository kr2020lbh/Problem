import sys
sys.stdin = open("input.txt", "r")


N = int(input())
B = [int(input()) for _ in range(N)]
B = [0] + B
ans = []
for i in range(1,N+1):
    start = i
    end = B[start]
    if start == end:
        ans.append(start)
    else:
        visited = [0]*N
        visited[start] = 1
        while True:
            if visited[end] == 1:
                break
            start = end
            end = B[start]

        ans.append(i)
print(len(ans))
print(*ans,sep='\n')
