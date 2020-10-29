import sys
sys.stdin = open("input.txt","r")
for t in range(int(input())):
    N = int(input())
    B = list(map(int,input().split()))
    B = [0] + B
    ans = [0] * 100001
    fail = [0] *100001
    for i in range(1,N+1):
        if i == B[i]:
            ans[i] = 1

    for i in range(1, N + 1):
        visited = [0] * (N+1)
        tmp = [i]
        start = B[i]
        flag = True


        cnt = 0
        while cnt < 100000:
            tmp.append(start)
            if ans[start] == 1 or visited[start] == 1 or fail[start] == 1:
                break
            if i == start:
                flag = False
                break
            else:
                visited[start] = 1
                start = B[start]
                cnt += 1

        if flag == False:
            for t_idx in tmp:
                ans[t_idx] = 1
        else:
            for t_idx in tmp:
                fail[t_idx] = 1
    cnt =0
    for i in range(1,100001):
        if ans[i]:
            cnt += 1
    print(N-cnt)
