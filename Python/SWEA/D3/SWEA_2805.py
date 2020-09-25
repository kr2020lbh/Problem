#2805. 농작물 수확하기
import sys
sys.stdin = open("input.txt","r")
for t in range(1,int(input())+1):
    N = int(input())

    middle = (N+1)//2
    result = 0
    erases = [2*i-1 for i in range(1,middle+1)]
    erases.extend([erases[-i-1] for i in range(1,middle)])

    for erase in erases:
        numbers = list(map(int,input()))
        result+=sum(numbers[middle-1-(erase-1)//2:middle+(erase-1)//2])

    print(f'#{t} {result}')