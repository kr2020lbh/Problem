import sys
sys.stdin = open("input.txt", "r")
def f(x,y):
    cnt = 0
    Q = [y]
    visited = [0] * (1000001)
    while True:
        tmp_set = set()
        cnt += 1
        for tmp in Q:
            visited[tmp] = 1
            if tmp - 1 == x or tmp + 1 == x or tmp + 10 == x:
                return cnt
            if tmp % 2 == 0:
                if tmp //2 == x:
                    return cnt
                if tmp//2 > 0 and visited[tmp//2] == 0:
                    tmp_set.add(tmp//2)

            if tmp+10 < 1000001 and visited[tmp+10] == 0:
                tmp_set.add(tmp + 10)

            if visited[tmp-1] == 0:
                tmp_set.add(tmp-1)

            if tmp+1 < 1000001 and visited[tmp+1] == 0:
                tmp_set.add(tmp+1)
        Q = tmp_set

for t in range(1,int(input())+1):
    N,M = map(int,input().split())
    print("#{} {}".format(t,f(N,M)))