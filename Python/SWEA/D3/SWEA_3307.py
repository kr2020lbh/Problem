#최장 증가 부분 수열
import sys
sys.stdin = open("input.txt","r")

for t in range(1,int(input())+1):
    N = int(input())
    lis = [1]*N
    arr = list(map(int, input().split()))
    for i in range(1,N): 
        for j in range(i):
            if arr[j]<arr[i]:
                lis[i] = max(lis[i], lis[j]+1)
        
    
    print(f'#{t} {max(lis)}')




# [1 1 2 1 3 4 1]
# 가장 큰 D 리스트의 인덱스에 있는 수 와 비교한다!!
# [1 3 2 5 4 ]
# [1 2 1 2 1]

# 2
# 5
# 1 3 2 5 4 
# 6
# 4 2 3 1 5 6