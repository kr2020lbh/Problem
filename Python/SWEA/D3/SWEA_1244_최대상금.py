import sys
sys.stdin = open("input.txt", "r")

# for t in range(1, int(input()) + 1):
#     nums, time = input().split()
    # for i in range(len(nums)-1):
    #     MAX = nums[i]
    #     idx = i
    #     if time == 0:
    #         break
    #     for j in range(i+1,len(nums)):
    #         if MAX <= nums[j]:
    #             MAX = nums[j]
    #             idx = j
    #     if idx != i:
    #         nums[i],nums[idx] = nums[idx],nums[i]
    #         time -= 1
    # if time%2 !=0:
    #     if len(set(nums)) == len(nums):
    #         nums[-1],nums[-2] = nums[-2],nums[-1]
    #
    #
    # print("#{}".format(t),end=' ')
    # print(*nums,sep='')


def select(cur_time,time,selection):
    global MAX
    if cur_time == time:
        tmp = nums[::]
        for s in selection:
            tmp[s[0]],tmp[s[1]] = tmp[s[1]],tmp[s[0]]
        tmp_max = int(''.join(tmp))
        if MAX < tmp_max:
            MAX = tmp_max
    else:
        for i in range(len(switches)):
            select(cur_time+1,time,selection+[switches[i]])


for t in range(1,int(input())+1):
    nums,time = input().split()
    nums=list(nums)
    time = int(time)
    if time>6:
        time = 6
    switches = []
    MAX = 0
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            switches.append([i, j])
    select(0,time,[])
    print("#{} {}".format(t,MAX))
