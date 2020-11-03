import sys
sys.stdin = open("input.txt", "r")

def binary_search(l,r,number):
    global cnt
    prev = -1
    while l <= r:
        mid = (l+r) // 2
        if N[mid] == number:
            cnt += 1
            break
        elif N[mid] > number:
            now = 0
            r = mid -1
        else:
            now = 1
            l = mid + 1
        if prev == now:
            break
        prev = now


for t in range(1,int(input())+1):
    n,m = map(int,input().split())
    N = list(map(int,input().split()))
    M = list(map(int,input().split()))
    cnt = 0
    for number in M:
        binary_search(0,n-1,number)
    print("#{} {}".format(t,cnt))