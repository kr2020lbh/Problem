'''
0 0001101
1 0011001
2 0010011
3 0111101
4 0100011
5 0110001
6 0101111
7 0111011
8 0110111
9 0001011
'''


import sys
sys.stdin =open("input.txt","r")
code = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9,
}

for t in range(1,int(input())+1):

    N,M = map(int,input().split())
    arr = [input() for _ in range(N)]
    mycode = ''
    secret = []

    for a in arr:

        for i in range(M-1,-1,-1):
            if a[i] == '1':
                mycode = a[i-55:i+1]
                break

        if mycode:
            for k in range(0,50,7):
                secret+=[code[mycode[k:k+7]]]
            break

    odd_sum = even_sum = 0

    for i in range(len(secret)-1):
        if (i+1)%2:
            odd_sum+=secret[i]
        else:
            even_sum+=secret[i]
    total = odd_sum*3 + even_sum + secret[-1]

    print("#{} ".format(t),end='')
    if total % 10 == 0:
        print(sum(secret))
    else:
        print(0)


