import sys
sys.stdin = open("input.txt","r")

def check():
    global start
    for element in nums[start+1::]:
        if element[0] > nums[start][0]:
            nums.append(nums[start])
            start+=1
            return False
    else:
        start+=1
        return True



for t in range(1,int(input())+1):
    N,M = map(int,input().split())
    nums = list(map(int,input().split()))
    nums = [[nums[i],False] for i in range(N)]
    nums[M][1]=True
    start = 0
    cnt=0
    while start<len(nums):
        if check():
            cnt+=1
            if nums[start-1][1]:
                print(cnt)