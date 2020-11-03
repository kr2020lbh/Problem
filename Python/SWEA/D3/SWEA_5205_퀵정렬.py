import sys
sys.stdin = open("input.txt","r")

def hoare_quick_sort(l,r):
    pivot = nums[l]
    i = l+1
    j = r

    while i<=j:
        while i <= j and nums[i] <= pivot: i+=1
        while i <= j and nums[j] >= pivot: j-=1
        if i < j: nums[i],nums[j] = nums[j],nums[i]
    nums[l],nums[j] = nums[j],nums[l]

    if l < j-1:hoare_quick_sort(l,j-1)
    if j+1 < r:hoare_quick_sort(j+1,r)


def lomuto_quick_sort(l,r):
    pivot = nums[r]
    i = l-1
    for j in range(l,r):
        if nums[j] <= pivot:
            i+=1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[r] = nums[r], nums[i+1]
    if l < i:lomuto_quick_sort(l,i)
    if i+2<r:lomuto_quick_sort(i+2,r)

for t in range(1,int(input())+1):
    N = int(input())
    nums = list(map(int,input().split()))
    lomuto_quick_sort(0,len(nums)-1)
    print("#{} {}".format(t,nums[len(nums)//2]))