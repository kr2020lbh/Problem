import sys
sys.stdin =open("input.txt","r")
code = [
    list('0001101'), #0
    list('0011001'), #1
    list('0010011'), #2
    list('0111101'), #3
    list('0100011'), #4
    list('0110001'), #5
    list('0101111'), #6
    list('0111011'), #7
    list('0110111'), #8
    list('0001011'), #9
]

for t in range(int(input())):
    N,M = map(int,input().split())
    arr = [input() for _ in range(N)]
    for hexa_code in arr:
        hexa_code = hexa_code.strip('0')
        binary_code = ''
        for hexa in hexa_code:
            binary = str(bin(int(hexa,16)))[2::]
            binary_code += '0'*(4-len(binary))+binary

        sentence = binary_code.rstrip('0').lstrip('0')
        while len(sentence)%7 != 0:
            sentence = '0' + sentence
        print(len(sentence))
