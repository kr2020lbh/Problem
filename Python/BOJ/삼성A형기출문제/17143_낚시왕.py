import sys
sys.stdin = open("input.txt", "r")

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


def move_shark():
    for i in range(len(sharks)):
        r, c, s, d, z = sharks[i]
        for j in range(s):
            nr, nc = r + dr[d], c + dc[d]
            if 0 > nr or nr >= row or 0 > nc or nc >= col:
                if d < 2:
                    d = (d+1) % 2
                else:
                    d = (d-1) % 2 + 2

                nr, nc = r + dr[d], c + dc[d]

            r, c = nr, nc
        sharks[i] = [r, c, s, d, z]


def eat_shark():
    eats = []
    idx = 0
    while idx < len(sharks):
        r, c, s, d, z = sharks[idx]
        next_idx = idx + 1
        while next_idx < len(sharks):
            r0, c0, s, d, z = sharks[next_idx]
            if r == r0 and c == c0:
                sharks.pop(next_idx)
            else:
                break
        idx += 1


def get_shark(j):
    global ans
    for i in range(len(sharks)):
        if sharks[i][1] == j:
            r, c, s, d, z = sharks.pop(i)
            ans += z
            return


row, col, M = map(int, input().split())
ans = 0
sharks = []
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    r -= 1
    c -= 1
    d -= 1
    sharks.append([r, c, s, d, z])

sharks.sort(key=lambda x: (x[0], x[1], -x[4]))
for c in range(col):
    get_shark(c)
    move_shark()
    sharks.sort(key=lambda x: (x[0], x[1], -x[4]))
    eat_shark()
print(ans)
