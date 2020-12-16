import sys
sys.stdin = open("input.txt","r")
N = int(input())
nums = list(map(int,input().split()))
if N < 3:
    if N == 1:
        print("A")
    else:
        if nums[0] == nums[1]:
            print(nums[0])
        else:
            print('A')
else:
    flag = True
    n1,n2,n3 = nums[0], nums[1], nums[2]
    k1,k2 = nums[1] - nums[0], nums[2] - nums[1]
    if k1 == 0:
        a = 0
        b = n1
    else:
        a = k2//k1
        b = n2 - n1 * a
    for i in range(N-1):
        n1,n2 = nums[i],nums[i+1]
        if n2 != n1*a + b:
            flag = False
            break
    if flag:
        print(nums[-1]*a + b)
    else:
        print('B')





