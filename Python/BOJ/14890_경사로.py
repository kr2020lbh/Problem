import sys
sys.stdin = open("input.txt","r")

def check(row):
    #높이 차가 1일 때만 가능하다.
    #높이가 낮아질때와 높아질때로 나누어 생각해본다
    #나와 이전이 같은 것의 개수를 계속 카운트한다
    global ans
    cnt = i = 1
    prev = row[0]
    while i <N :
        cur = row[i]
        if cur == prev:
            cnt += 1
        else:
            if abs(cur-prev) > 1:
                return
            if cur-prev == 1: #높아질때는 그전에 prev와 같은 것의 개수가 X보다 작으면 안된다.
                if cnt < X:
                    return
                cnt = 1
            else: #낮아질 때는 앞으로 cur와 같은 높이의 수가 X보다 작으면 안된다. 또한 이들을 경사로에 썼으니 건너뛰어야한다
                #현재 index : i
                #i부터 i+X-1 인덱스까지 높이가 같아야한다.
                if N < i+X:
                    return
                for j in range(i+1,i+X):
                    if cur != row[j]:
                        return
                i = i+X-1
                cnt = 0
        prev = row[i]
        i += 1
    ans += 1

N,X = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
ans = 0
#세로줄을 가로줄로
maps += list(zip(*maps))
for row in maps:
    check(row)
print(ans)

