N = input()
nums = [0] * 10
for n in N:
    nums[int(n)]+=1
for i in range(9,-1,-1):
    if nums[i]!=0:
        print(str(i)*nums[i],end='')
