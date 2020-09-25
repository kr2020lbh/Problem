#1860. 진기의 최고급 붕어빵
import sys
sys.stdin = open("input.txt","r")

no='Impossible'
yes='Possible'
result=[]
for t in range(1,int(input())+1):
    N,M,K = map(int,input().split()) #N명 M초 동안 K개의 붕어빵
    times = sorted(list(map(int,input().split())))

    prev_time = times[0]
    if times[0] < M:
        result.append(no)

    else:
        for i in range(1,N):
            time = times[i]-prev_time
            if (times[i]//M) * K > i  or time >= M:
                prev_time = times[i]
                continue
            else:
                result.append(no)
                break
        else:
            result.append(yes)
for i in range(len(result)):
    print(f'#{i+1} {result[i]}')