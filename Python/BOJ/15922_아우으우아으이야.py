import sys
sys.stdin = open("input.txt","r")
N = int(input())
lines = []
for _ in range(N):
    lines.append(list(map(int,input().split())))
prev_s, prev_e = lines[0]
line = prev_e-prev_s
if N == 1:
    print(line)
else:
    for i in range(1,N):
        cur_s,cur_e = lines[i]
        if cur_s < prev_e:
            if cur_e < prev_e:
                continue
            else:
                line += (cur_e - prev_e)
        else:
            line += (cur_e - cur_s)
        prev_s,prev_e = cur_s,cur_e
    print(line)


