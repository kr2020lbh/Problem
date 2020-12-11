import sys
sys.stdin = open("input.txt","r")
def check(numbers):
    for i in range(N-1):
        if numbers[i] == numbers[i+1][0:len(numbers[i])]:
            print("NO")
            return
    print("YES")

for t in range(int(input())):
    N = int(input())
    numbers = [input() for _ in range(N)]
    sorted_numbers = sorted(numbers,key=lambda x:(x,len(x)))
    check(sorted_numbers)
