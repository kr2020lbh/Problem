#1966 숫자를 정렬하자
import sys
import time
sys.stdin = open("input.txt","r")
def bubble_sort():
    for i in range(N-1):
        for j in range(i+1,N):
            if nums[i]>nums[j]:
                nums[i],nums[j] = nums[j],nums[i]

def selection_sort():
    for i in range(N-1):
        minIndex = i
        for j in range(i+1,N):
            if nums[minIndex]>nums[j]:
                minIndex = j
        nums[i],nums[minIndex] = nums[minIndex],nums[i]
start = time.time()
for t in range(1,int(input())+1):
    N = int(input())
    nums = list(map(int,input().split()))
    bubble_sort()
    print(f'#{t}',end=' ')
    [print(str(num),end=' ') for num in nums]
    print()
print("time :", time.time() - start)