import sys
sys.stdin = open("input.txt","r")

def check(road):
    global ans
    prev = road[0]
    cnt = i = 1

    while i < N:
        cur = road[i]
        if prev == cur: #이전 땅과 높이가 같다면 cnt 갱신
            cnt += 1
        else:
            # 높이 차가 2 이상일때는 끝
            if abs(prev - cur) > 1:
                return

            # 높이 차가 1일 때
            if prev-cur == 1: # 높이가 낮아질떄
                if i+X > N: #경사대를 놓을 수 없으면 끝
                    return

                for j in range(i,i+X): #경사대를 놓기 위해 같은 높이 땅이 X개 없으면 끝
                    if road[j] != cur:
                        return

                i += X-1 # 경사도를 놓은 땅은 건너 뛴다
                cnt = 0
            else: # 높이가 높아질떄
                if cnt < X: # 그 전에 같은 높이의 땅이 X개 없으면 끝
                    return
                cnt = 1 # 다른 높이의 땅을 만났으니 1로 초기화
        prev = road[i] # prev 값 갱신
        i+=1 # 다음 땅으로 이동
    ans+=1  # 모두 만족하면 1 더하기

for t in range(1,int(input())+1):
    N,X = map(int,input().split())
    roads = [list(map(int,input().split())) for _ in range(N)]
    roads_col = list(zip(*roads))
    ans = 0
    for i in range(N):
        row,col = roads[i], roads_col[i]
        check(row)
        check(col)
    print("#{} {}".format(t,ans))
