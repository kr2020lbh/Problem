import sys
sys.stdin = open("input.txt","r")


def get_idx(first, last):
    MAX = 0
    for idx in range(first, last + 1):
        if arr[idx] >= MAX:
            MAX = arr[idx]
            IDX = idx
    return IDX, MAX


arr = [0] * 1001
indexes = []

arr = [0] * 1001
for _ in range(int(input())):
    index, height = map(int, input().split())
    indexes.append(index)
    arr[index] = height

left = min(indexes)
right = max(indexes)

max_idx = get_idx(left, right)[0]
max_height = get_idx(left, right)[1]

left_max = right_max = 0
L = []
R = []

while left != max_idx:
    if arr[left] > left_max: left_max = arr[left]
    L.append(left_max)
    left += 1

while right != max_idx:
    if arr[right] > right_max: right_max = arr[right]
    R.append(right_max)
    right -= 1

print(sum(L + R) + max_height)


#
# def get_idx(first,last):
#     MAX = 0
#     for idx in range(first,last+1):
#         if arr[idx] >= MAX:
#             MAX = arr[idx]
#             IDX = idx
#     return [IDX,MAX]
#
# arr = [0] * 1001
# n = int(input())
# indexes = []
# arr = [0] * 1001
# for _ in range(n):
#     index,height = map(int,input().split())
#     indexes.append(index)
#     arr[index] = height
#
# indexes.sort()
# first,last = indexes[0],indexes[-1]
#
# ans=[get_idx(first,last)]
#
# max_idx = ans[0][0]
# max_height = ans[0][1]
# left = []
# right = []
# while True:
#     if max_idx == first:
#         break
#     tmp=get_idx(first,max_idx-1)
#     left.append(tmp)
#     max_idx=tmp[0]
#
# max_idx = ans[0][1]
# while True:
#     if max_idx == last:
#         break
#     tmp=get_idx(max_idx+1,last)
#     right.append(tmp)
#     max_idx=tmp[0]
#
# print(ans)
#
# res = ans[0][1]*(last-first+1)
# left = left[::-1] + ans
# print(left,right)
# left_before = left[0]
#
# for l in left[1::]:
#     print((l[0]-left_before[0])*left_before[1])
#     left_before = l

