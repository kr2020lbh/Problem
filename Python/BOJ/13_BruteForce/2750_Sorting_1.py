import sys
sys.stdin = open("input.txt","r")
N=int(input())
result = []
for i in range(N):
    new_number = int(input())
    for idx,old_number in enumerate(result):
        if old_number>new_number:
            result.insert(idx,new_number)
            break
    else:
        result.append(new_number)
[print(number) for number in result]