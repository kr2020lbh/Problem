import sys
sys.stdin = open("input.txt","r")
# def solution():
#     i = j = 0
#     while True:
#         if arr1[i] == 'end':
#             return 2,j
#         if arr2[j] == 'end':
#             return 1,i
#         if arr1[i] < arr2[j]:
#             res.append(arr1[i])
#             i += 1
#         else:
#             res.append(arr2[j])
#             j += 1

# N,M = map(int,input().split())
# arr1 = list(map(int,input().split())) + ['end']
# arr2 = list(map(int,input().split())) + ['end']
# res = []
# id,idx = solution()
# if id == 1:
#     res += arr1[idx:-1:]
# else:
#     res += arr2[idx:-1:]
# print(*res)

N,M = map(int,input().split())
arr = list(map(int,input().split())) + list(map(int,input().split()))
print(' '.join((map(str,sorted(arr)))))