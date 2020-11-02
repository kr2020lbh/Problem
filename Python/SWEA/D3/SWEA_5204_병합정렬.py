import sys
sys.stdin = open("input.txt","r")
def mergeSort(l):
    if len(l) == 1:return l
    mid = len(l)//2
    left = mergeSort(l[0:mid])
    right = mergeSort(l[mid:])
    return merge(left,right)

def merge(left,right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    tmp = []
    i=j=0
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            tmp.append(left[i])
            i += 1
            continue

        if left[i] >= right[j]:
            tmp.append(right[j])
            j += 1
            continue

    while i < len(left):
        tmp.append(left[i])
        i += 1

    while j < len(right):
        tmp.append(right[j])
        j += 1

    return tmp


for t in range(1,int(input())+1):
    N = int(input())
    L = list(map(int,input().split()))
    cnt = 0
    L=mergeSort(L)
    print("#{} {} {}".format(t,L[N//2],cnt))
