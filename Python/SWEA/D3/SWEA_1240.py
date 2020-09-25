#1240. [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드
import sys
sys.stdin = open("input.txt","r")
decodes = ['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
for t in range(1,int(input())+1):
    row,col = map(int,input().split())
    serial_num = []
    for i in range(row):
        bin_code = input()
        if bin_code!='0'*col:
            for j in range(col):
                if bin_code[j:j+7] in decodes and bin_code[j+7:j+14] in decodes:
                    while len(serial_num) != 8:
                        for k in range(10):
                            if decodes[k] == bin_code[j :j+7]:
                                serial_num.append(k)
                        j+=7
                    break
                j += 1
    odd_sum = 0
    even_sum = 0
    for i in range(7):
        if i%2:
            even_sum+=serial_num[i]
        else:
            odd_sum+=serial_num[i]
    if (even_sum+odd_sum*3+serial_num[-1])%10==0:
        result = sum(serial_num)
    else:
        result = 0
    print(f'#{t} {result}')