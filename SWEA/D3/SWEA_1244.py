#1244. [S/W 문제해결 응용] 2일차 - 최대 상금
import sys
sys.stdin = open("input.txt","r")

for t in range(1,int(input())+1):
    nums, N = map(int,input().split())
    nums = list(map(int,str(nums)))
    for i in range(len(nums)):
        if N==0:break
        else:
            MAX = nums[i]
            MAX_IDX = i
            MIN = nums[i]
            MIN_IDX = i
            for j in range(i,len(nums)):
                if nums[j] >= MAX:
                    MAX = nums[j]
                    MAX_IDX = j
                if nums
            if MAX_IDX != i and nums[i]!=nums[MAX_IDX]:
                nums[i],nums[MAX_IDX] = nums[MAX_IDX],nums[i]
                N-=1
    else:
        if N%2==1:
            #똑같은 숫자가 없는 경우
            if len(set(nums)) == len(nums):
                print(set(nums),nums)
                nums[-1],nums[-2] = nums[-2],nums[-1]
            #똑같은 숫자가 있는 경우

    ans = ''.join(list(map(str,nums)))
    print(f'#{t} {ans}')


