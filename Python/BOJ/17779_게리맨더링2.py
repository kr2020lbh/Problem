import sys
sys.stdin = open("input.txt","r")
N = int(input())
maps = []
for _ in range(N):
    row = list(map(int,input().split()))
    maps.append(row)

answer = 99999
for i in range(N-2):
    for j in range(1,N-1):
        up,left,down,right = [i,j],[i+1,j-1],[i+2,j],[i+1,j+1]
        P = min(min(i,N-j),min(i+1,N-(j+1)))#오른쪽 위로 가는 것 중 짧은 것
        Q = min(min(N-(i+2),N-(j)),min(N-(i+1),N-(j+1)))#오른쪽 아래로 가는 것 중 짧은것
        for p in range(P+1):
            for q in range(Q+1):
                maps_section = [[0] * N for _ in range(N)]

                if 0< i+1-p+q < N and 0< j+1+p+q< N and 0< i+2+q < N and 0< j+q < N:
                    res = [0,0,0,0,0]
                    left = [i + 1, j - 1]
                    maps_section[left[0]][left[1]] = 5
                    for _p in range(p+1):
                        up = [i - _p, j + _p]
                        maps_section[up[0]][up[1]] = 5
                        right = [i + 1 - _p + q, j + 1 + _p + q]
                        maps_section[right[0]][right[1]] = 5
                    for _q in range(q+1):
                        down = [i + 2 + _q, j + _q]
                        maps_section[down[0]][down[1]] = 5
                        right = [i + 1 - p + _q, j + 1 + p + _q]
                        maps_section[right[0]][right[1]] = 5

                    visited = [[0]*N for _ in range(N)]
                    for r in range(left[0]):
                        for c in range(up[1]+1):
                            if maps_section[r][c] == 5:
                                break
                            else:
                                maps_section[r][c] = 1
                                res[0] += maps[r][c]
                                visited[r][c] = 1

                    for r in range(left[0],N):
                        for c in range(down[1]):
                            if maps_section[r][c] == 5:
                                break
                            else:
                                maps_section[r][c] = 3
                                res[2] += maps[r][c]
                                visited[r][c]= 1

                    for r in range(right[0]+1):
                        for c in range(N-1,up[1],-1):
                            if maps_section[r][c] == 5:
                                break
                            else:
                                maps_section[r][c] = 2
                                res[1] += maps[r][c]
                                visited[r][c] =1

                    for r in range(right[0]+1,N):
                        for c in range(N-1,down[1]-1,-1):
                            if maps_section[r][c] == 5:
                                break
                            else:
                                maps_section[r][c] = 4
                                res[3] += maps[r][c]
                                visited[r][c] =1

                    for r in range(N):
                        for c in range(N):
                            if not visited[r][c]:
                                maps_section[r][c] = 5
                                res[4] += maps[r][c]

                    ans = max(res) - min(res)
                    if answer > ans:
                        answer = ans

print(answer)