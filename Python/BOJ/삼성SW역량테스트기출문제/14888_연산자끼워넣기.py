import sys
sys.stdin = open("input.txt","r")

from itertools import permutations

def cal(a,b):
    if a<0 and b>0 or a>0 and b<0:
        return -(abs(a)//abs(b))
    else:
        return a//b

N = int(input())
nums = list(map(int,input().split()))
num_operators = list(map(int,input().split()))
plus,minus,multiple,divide = num_operators

operators = ''
operators += '+' * plus
operators += '-' * minus
operators += '*' * multiple
operators += '/' * divide
minVal,maxVal = None,None
for perm in set(permutations(list(operators))):
    tmp = nums[0]
    for i in range(len(perm)):
        if perm[i] == '+':
            tmp += nums[i+1]
        elif perm[i] == '-':
            tmp -= nums[i+1]
        elif perm[i] == '/':
            tmp = cal(tmp,nums[i+1])
        else:
            tmp *= nums[i+1]
    minVal = min(minVal,tmp) if minVal != None else tmp
    maxVal = max(maxVal,tmp) if maxVal != None else tmp 
print(maxVal)
print(minVal)