#Base64 Decoder
import sys
sys.stdin = open("input.txt","r")

def input_str_to_3_words():
    words = []
    for i in range(0,len(encoding),3):
        words.append(encoding[i:i+3])
    return words

def words_to_24bits(words):
    result = []
    bits24 = [0]*24

    for word in words:
        nums = []
        i = 0
        for char in word:

            bit_place = 7
            num = ord(char)
            nums.append(num)
            while bit_place>=0:

                if num//(2**bit_place):
                    bits24[i] = num // (2 ** bit_place)
                    num-=(2 ** bit_place)
                bit_place-=1
                i+=1
        print(bits24,word,nums)
        result.append(bits24)
    return result

def split_bits24_to_bits6 (bits24):
    for bit24 in bits24:
        for i in range(0,24,6):
            bit6 = bit24[i:i+6]



decodes = []
[ decodes.append(chr(i+65)) for i in range(26)]
[ decodes.append(chr(i+97)) for i in range(26)]
[ decodes.append(str(i)) for i in range(10)]
decodes.extend('+/')


for t in range(1,int(input())+1):
    encoding = input()
    result = []
    words = input_str_to_3_words()
    print(words)
    # for j in range(len(words)):
    #     bits_24[j*8:(j+1)*8] =word_to_8bits(words[j])
    #     result1 =split_24bits_to_6bits(bits_24)
    #     for i in range(len(result1)):
    #         result.append(decodes[result1[i]])
    words_to_24bits(words)







