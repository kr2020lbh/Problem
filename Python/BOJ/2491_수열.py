import sys
sys.stdin = open("input.txt","r")

n = int(input())
arr1 = list(map(int, input().split()))
MAX = 1

length = 1
for i in range(1, n):
    if arr1[i - 1] <= arr1[i]:
        length += 1
    else:
        length = 1
    if MAX < length:
        MAX = length
length = 1
for i in range(1, n):
    if arr1[i - 1] >= arr1[i]:
        length += 1
    else:
        length = 1
    if MAX < length:
        MAX = length
print(MAX)