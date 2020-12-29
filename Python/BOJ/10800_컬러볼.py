import sys
sys.stdin = open("input.txt","r")
N = int(input())
balls = []
answer = [0]*N
sum_by_color = [0] * 200001
for i in range(N):
    color,size = map(int,sys.stdin.readline().split())
    balls.append([color,size,i])

balls.sort(key=lambda x:x[1])
total = j = 0
for i in range(N):
    while balls[j][1] < balls[i][1]:
        total += balls[j][1]
        sum_by_color[balls[j][0]] += balls[j][1]
        j += 1
    answer[balls[i][2]] = total - sum_by_color[balls[i][0]]

for _ in range(N):
    print(answer[_])

