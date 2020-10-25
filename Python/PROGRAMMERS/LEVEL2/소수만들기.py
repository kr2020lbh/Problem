from itertools import combinations

def is_prime(num):
    cnt = 1
    for i in range(1,int(num**(1/2))+3):
        if num % i == 0:
            cnt += 1
        if cnt > 2:
            return False
    return True



def select_three_num(nums,visited,sumation,idx):
    global answer
    if len(visited) == 3:
        if is_prime(sumation):
            answer += 1
    else:
        for i in range(idx,len(nums)):
            if i in visited:
                continue
            else:
                select_three_num(nums, visited + [i], sumation + nums[i],i)


def solution(nums):
    global answer
    select_three_num(nums,[],0,0)
    return answer
answer = 0
solution([1,2,7,6,4])



'''
from itertools import combinations

def is_prime(num):
    cnt = 1
    for i in range(1,int(num**(1/2))+3):
        if num % i == 0:
            cnt += 1
        if cnt > 2:
            return False
    return True


def solution(nums):
    answer = 0
    for c in combinations(nums,3):
        if is_prime(sum(c)):
            answer += 1

    return answer
'''