import sys
sys.stdin = open("input.txt","r")
N = int(input()) #색종이 수
indexes = [list(map(int,input().split())) for _ in range(N)] #왼쪽 하단 모서리의 좌표
whites = [[0]*100 for _ in range(100)]
for C,R in indexes:
    for r in range(100-R-10,100-R):
        for c in range(C,C+10):
            whites[r][c] = 1
ans = 0
for r in range(100):
    for c in range(100):
        if whites[r][c] == 1:
            for d_r,d_c in [[1,0],[0,1],[-1,0],[0,-1]]:
                dr = r + d_r
                dc = c + d_c
                if not (0<= dr < 100 and 0<= dc < 100):
                    ans += 1
                    continue
                if whites[dr][dc] == 0:
                    ans += 1
print(ans)

# [print(w) for w in whites]
