import sys
sys.stdin = open("input.txt","r")

N = int(input())
schedules = [list(map(int,input().split())) for _ in range(N)]
schedules.sort(key=lambda x:(x[1],x[0]))
print(schedules)
cnt = 0
end = 0
for i in range(N):
    if end <= schedules[i][0]:
        end = schedules[i][1]
        cnt+=1
print(cnt)



