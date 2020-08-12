#Base64 Decoder
import sys
sys.stdin = open("input.txt","r")

def word_to_8bits(word):
    num = ord(word)
    bits = []
    while len(bits)<8:
        bits.append(str(num%2))
        num//=2
    return bits[::-1]

def split_24bits_to_6bits(bits):
    numbers = []
    for i in range(4):

        bits_6 = ''.join(bits[i*6:(i+1)*6])

        numbers.append(int(bits_6,2))
    return numbers

decodes = []
[ decodes.append(chr(i+65)) for i in range(26)]
[ decodes.append(chr(i+97)) for i in range(26)]
[ decodes.append(str(i)) for i in range(10)]
decodes.extend('+/')


for t in range(1,int(input())+1):
    encoding = input()
    result = []
    for i in range(0,len(encoding),3):
        bits_24 = ['0']*24
        words = encoding[i:i+3]
        for j in range(len(words)):
            bits_24[j*8:(j+1)*8] =word_to_8bits(words[j])
            result1 =split_24bits_to_6bits(bits_24)
            for i in range(len(result1)):
                result.append(decodes[result1[i]])
    print(result)





