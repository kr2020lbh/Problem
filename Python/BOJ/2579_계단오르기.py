import sys
sys.stdin = open("input.txt","r")

def get_sum(stairs,cur_idx,cur_sum,continuous):
    global  MAX
    if MAX < cur_sum:
        MAX = cur_sum

    if cur_idx + 1 < len(stairs) and continuous == 1:
        get_sum(stairs,cur_idx+1,cur_sum+stairs[cur_idx+1],continuous+1)
    if cur_idx +2 < len(stairs):
        get_sum(stairs,cur_idx+2,cur_sum+stairs[cur_idx+2],1)

n = int(input())
stairs = [ int(input()) for _ in range(n)]
dp = []
if n < 3:
    if n == 1:
        print(stairs[0])
    else:
        print(sum(stairs))
else:
    dp.append(stairs[0])
    dp.append(stairs[0] + stairs[1])
    dp.append(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))
    for i in range(3,n):
        dp.append(max(dp[i-3] + stairs[i] + stairs[i-1], stairs[i] + dp[i-2]))
    print(dp[-1])
