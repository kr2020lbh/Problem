#0/1 Knapsack
import sys
sys.stdin = open("input.txt","r")
# 가장 중요한 포인트
# max(넣을 아이템의 가치,
#   + 가방의 부피에서 넣을 아이템의 부피를 뺐을 때의 최대 가치
#   , 아이템을 안넣을 때의 가치       )
for t in range(1, int(input())+1):
    num_of_items,volume_of_bag = map(int,input().split())
    cost_list = [ [ 0 for _ in range(volume_of_bag+1)] for _ in range(num_of_items)]
    max_of_cost = 0
    for i in range(num_of_items):
        volume, cost = map(int,input().split())
        if i == 0:
            cost_list[0][volume:volume_of_bag+1] = [cost]*(volume_of_bag-volume+1)
            continue
        for j in range(1,volume_of_bag+1):
            
            if volume > j:
                cost_list[i][j] = cost_list[i-1][j]
            else:
                cost_list[i][j] = max(cost + cost_list[i-1][j-volume], cost_list[i-1][j])
        if max_of_cost< cost_list[i][j]:
            max_of_cost = cost_list[i][j]
    print(f'#{t} {max_of_cost}')