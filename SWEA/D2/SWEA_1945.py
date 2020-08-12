#간단한 소인수분해
import sys
sys.stdin = open("input.txt","r")
nums =[2,3,5,7,11]
for t in range(1,int(input())+1):
    N=int(input())
    result=''
    for num in nums:
        count = 0
        while N%num==0:
            count+=1
            N//=num
        result+=str(count)+' '
    print(f'#{t} {result}')