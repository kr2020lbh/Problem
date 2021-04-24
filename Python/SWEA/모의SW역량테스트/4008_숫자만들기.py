import sys
sys.stdin = open("input.txt","r")

# def permutations(arr,N):
#     def generator(arr,N,v,tmp):
#         if len(tmp) == N:
#             result.append(tmp)
#             return
#         for i in range(len(arr)):
#             if not v[i] and (i == 0 or arr[i-1] != arr[i] or v[i-1]):
#                 v[i] = 1
#                 generator(arr,N,v,tmp + [arr[i]])
#                 v[i] = 0

#     arr = sorted(arr)
#     v = [0]*len(arr)
#     result = []
#     generator(arr,N,v,[])
#     return result

def calculate(perm):
    res = nums[0]
    for i in range(len(perm)):
        if perm[i] == '+':
            res += nums[i+1]
        if perm[i] == '-':
            res -= nums[i+1]
        if perm[i] == '*':
            res *= nums[i+1]
        if perm[i] == '/':
            res = int(res/nums[i+1])
    return res


def cal(a,b,i):
    if i==0:
        a += b
    if i==1:
        a -= b
    if i==2:
        a *= b
    if i==3:
        a = int(a/b)
    return a


def dfs(idx,res):
    global max_val,min_val
    if idx == N-1:
        max_val = max(max_val,res)
        min_val = min(min_val,res)
        return
    for i in range(4):
        if operators[i]:
            operators[i] -= 1
            dfs(idx+1,cal(res,nums[idx+1],i))
            operators[i] += 1


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    operators = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    max_val = -100000000
    min_val = 100000000
    possibles = []
    dfs(0,nums[0])
    print("#{} {}".format(tc,max_val-min_val))