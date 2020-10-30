import sys
sys.stdin = open("input.txt","r")

def solution(idx,value):
    global min_value
    global max_value
    if idx == N-1:

        if value >= max_value:
            max_value = value
        if value <= min_value:
            min_value = value
        return
    else:
        for i in range(4):
            if operators[i] > 0:
                operators[i] -= 1
                if i == 0:
                    n_value = value + nums[idx + 1]
                elif i == 1:
                    n_value = value - nums[idx + 1]
                elif i == 2:
                    n_value = value * nums[idx + 1]
                else:
                    n_value = int(value / nums[idx + 1])
                solution(idx+1,n_value)
                operators[i]+=1


for t in range(1,int(input())+1):
    N = int(input())
    operators= list(map(int,input().split()))
    nums = list(map(int,input().split()))
    min_value = 100000000
    max_value = -100000000
    solution(0,nums[0])
    print("#{} {}".format(t,max_value-min_value))