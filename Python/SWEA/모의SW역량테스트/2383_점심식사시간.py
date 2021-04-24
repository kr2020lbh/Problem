import sys
sys.stdin = open("input.txt","r")


def set_start(depth):
    global ans
    if depth == len(p):
        ans = min(ans,go(p))
        return
    for i in range(2):
        p[depth].append(i)
        set_start(depth+1)
        p[depth].pop()


def go(indexes):
    stair1 = []
    stair2 = []
    for r,c,flag in indexes:
        sr,sc,k = s[flag]
        distance = abs(r-sr) + abs(c-sc)
        stair1.append([distance,k+1]) if flag == 0 else stair2.append([distance,k+1])
    stair1.sort(key=lambda x:-x[0])
    stair2.sort(key=lambda x:-x[0])

    return max(stair_logic(stair1),stair_logic(stair2))

def stair_logic(stair):
    going_down = []
    waiting = set()
    time = 0
    while len(stair) or len(going_down):
        time += 1
        for i in range(len(going_down)-1,-1,-1):
            going_down[i][1] -= 1
            if going_down[i][1] == 0:
                going_down.pop(i)
        for i in range(len(stair)-1,-1,-1):
            if stair[i][0] <= time:
                if len(going_down) >= 3:
                    waiting.add(tuple)
                    break
                else:
                    going_down.append(stair[i])
                    stair.pop(i)

    return time



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    p = []
    s = []
    ans = 10**5
    for i in range(N):
        row = list(map(int,input().split()))
        for j in range(N):
            if row[j] == 1:
                p.append([i,j])
            elif row[j] != 0:
                s.append([i,j,row[j]])
    set_start(0)
    print("#{} {}".format(tc,ans))