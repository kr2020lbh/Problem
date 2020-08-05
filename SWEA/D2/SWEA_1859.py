#백만 장자 프로젝트
import sys
sys.stdin = open("input.txt","r")

def check_ascending(a):
    if len(a)==1:return True
    else:
        prev = a[0]
        for i in range(1,len(a)):
            if prev>a[i]:
                return False
            prev = a[i]
        return True

for t in range(1,int(input())+1):
    N = int(input())
    prices = list(map(int,input().split()))
    start = 0
    arr = []
    cnt = 0
    while start<N:
        for end in range(start+1,N):
            if check_ascending(prices[start:end+1]):
                cnt+=1
   
            else:
                if len(prices[start:end])!=1:
                    arr.append(prices[start:end])
                start = end-1
                break
        
        else:            
            start+=1
    print(arr, cnt)