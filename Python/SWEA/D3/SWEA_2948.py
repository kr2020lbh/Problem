#문자열 교집합
import sys
sys.stdin = open("input.txt","r")

def binary_serach(arr,key):
    start = 0
    end = len(arr)-1
    while start<=end:
        middle = (start+end)//2
        if arr[middle]==key:return True
        elif arr[middle]<key:start = middle+1
        else:end = middle-1
    return False

for t in range(1,int(input())+1):
    a,b = map(int,input().split())
    list_a = list(map(str,input().split()))
    list_b = sorted(list(map(str,input().split())))

    count = 0
    for element in list_a:
        if binary_serach(list_b,element):
            count+=1
    print(f'#{t} {count}')



