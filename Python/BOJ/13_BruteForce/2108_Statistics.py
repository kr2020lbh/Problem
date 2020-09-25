import sys
from collections import Counter
sys.stdin = open("input.txt", "r")
N = int(sys.stdin.readline())
SUM = 0
numbers = []
for i in range(N):
    number = int(sys.stdin.readline())
    numbers.append(number)
    SUM += number

numbers.sort()
freq = sorted(Counter(numbers).items(),key=lambda x:(-x[1],x[0]) )
print(round(SUM/N))
print(numbers[N//2])
if N==1:
    print(number)
else:
    if freq[0][1]==freq[1][1]:
        print(freq[1][0])
    else:
        print(freq[0][0])
print(numbers[-1]-numbers[0])
