#1288 새로운 불면증 치료법
import sys
sys.stdin = open("input.txt","r")

for t in range(1,int(input())+1):
    N = int(input())
    zero_to_nine = [False]*10
    count = 1

    while sum(zero_to_nine) != 10:
        N_sheep = N * count
        str_N_sheep = str(N_sheep)

        for n in str_N_sheep:
            zero_to_nine[int(n)]=True

        count+=1

    print(f'#{t} {N_sheep}')


