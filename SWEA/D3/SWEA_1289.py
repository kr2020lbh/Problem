#1289. 원재의 메모리 복구하기
import sys
sys.stdin = open("input.txt","r")

for t in range(1,int(input())+1):
    bits=list(map(int,input()))
    prev = bits[0]
    while prev==0:
        bits.remove(0)
        prev = bits[0]

    count = 1
    for bit in bits[1:]:
        if bit != prev:
            prev = bit
            count+=1
    print(f'#{t} {count}')
'''
0011
100
110010
111001
1010101
'''