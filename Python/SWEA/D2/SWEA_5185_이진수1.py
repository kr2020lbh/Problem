import sys
sys.stdin =open("input.txt","r")
for t in range(1,int(input())+1):
    N,hexinput = input().split()
    hexinput = list(hexinput)
    binaryoutput = ''
    for hexa in hexinput:
        binaryoutput += '0'*(4-len(bin(int(hexa,16))[2::]))+bin(int(hexa,16))[2::]
    print("#{} {}".format(t,binaryoutput))

