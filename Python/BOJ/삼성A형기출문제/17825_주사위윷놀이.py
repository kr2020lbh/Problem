import sys
sys.stdin = open("input.txt","r")


def isSamePlace(markers,next_score,map_num,map_idx,i):
    for j in range(4):
        if i == j:
            continue
        if markers[j][0] !=0 and next_score == markers[j][0]:
            if next_score == 30 and markers[j][2] != map_idx:
                continue
            if map_num == markers[j][1]:
                return True
            if map_num != 0 and markers[j][1] != 0:
                return True
            if next_score == 40:
                return True
    return False

def dfs(dice_idx,sumation):
    global ans
    if dice_idx == 10:
        if ans < sumation:
            ans = sumation
        return
    for i in range(4):
        score, map_num0, map_idx0, local_sum0 = markers[i]
        if score == 0 and map_idx0 > 0:
            continue

        map_num = map_num0
        map_idx = map_idx0
        local_sum = local_sum0
        
        if map_num0 == 0:
            next_score = maps[map_idx0 + dice[dice_idx]]
            if next_score == 10:
                map_num = 10
                map_idx = 0
            if next_score == 20:
                map_num = 20
                map_idx = 0
            if next_score == 30:
                map_num = 30
                map_idx = 0
            if not (next_score == 10 or next_score == 20 or next_score == 30):
                map_idx = map_idx0 + dice[dice_idx]

        if map_num0 == 10:
            next_score = maps10[map_idx0 + dice[dice_idx]]
            map_idx = map_idx0 + dice[dice_idx]

        if map_num0 == 20:
            next_score = maps20[map_idx0 + dice[dice_idx]]
            map_idx = map_idx0 + dice[dice_idx]

        if map_num0 == 30:
            next_score = maps30[map_idx0 + dice[dice_idx]]
            map_idx = map_idx0 + dice[dice_idx]
        
        if isSamePlace(markers,next_score,map_num,map_idx,i):
            continue

        markers[i] = [next_score,map_num,map_idx,local_sum]
        dfs(dice_idx+1,sumation+next_score)
        markers[i] = [score, map_num0, map_idx0,local_sum0]
        

dice = list(map(int,input().split()))
markers = [[0,0,-1,0] for _ in range(4)] #말판 점수, 맵, idx, sumation
maps = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40] + [0] * 50
maps10 = [10,13,16,19,25,30,35,40] + [0] * 50
maps20 = [20,22,24,25,30,35,40] + [0] * 50
maps30 = [30,28,27,26,25,30,35,40] + [0] * 50
ans = 0
dfs(0,0)

print(ans)