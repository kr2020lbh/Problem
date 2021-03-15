import sys
sys.stdin = open("input.txt","r")
N = int(input())
nums = [[int(num),idx+1] for idx,num in enumerate(input().split())]
stack = [nums[0]]
ans = [0]
for i in range(1,N):
    cur_num = nums[i][0]
    while stack:
        last_num,last_idx = stack[-1]
        if last_num > cur_num:
            ans.append(last_idx)
            break
        else:
            stack.pop()
    if not stack:
        ans.append(0)
    stack.append(nums[i])
print(ans)
