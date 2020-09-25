#Base64 Decoder
import sys
import base64
sys.stdin = open("input.txt","r")
# 1byte = 8bit
# 문자를 3 byte 넣으면 24 bit
# 문제에서 얘기하는 Base64 Encoding은
# 3 byte의 문자를 각각 아스키코드로 변환하여 해당하는 숫자를
# 8bit의 2진수로 변환하고 이어서 24bit로 만든다.
# 이후 24 bit의 2진수를 6bit 씩 잘라 각각 해당하는 숫자를 표에서 확인하여
# 해당하는 문자로 바꿨을 때 이를 Base64 Encoding이라 한다.
# Encoding을 하면 3개의 문자가 4개로 바뀐다.

# 하지만 문제에서는 Decoding을 원한다. 즉 반대의 과정을 해야한다.
# 4개의 문자를 입력 받아 3개의 문자로 바꾸는 과정을 해야한다.
# 4개의 문자는 각각 decodes에 해당하는 값을 6bit로 바꾸고, 이어서 24bit로 만든다.
# 24bit를 다시 8bit로 잘라 10진수로 변환하고, 그 값을 아스키코드 변환하여 결과를 출력한다.

import pprint

decodes = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def splited_words_by4():
    result = []
    for i in range(0,len(words),4):
        result.append(words[i:i+4])
    return result


def decoding_4words(arr):
    result = []

    for words in arr:
        tmp=[]
        for char in words:
            for i in range(64):
                if decodes[i]==char:
                    tmp.extend([i])
        result.append(tmp)
    return result


def num_to_6bits(num):
    bit_place = 5
    btis6 = [0]*6
    i=0
    while bit_place>=0:
        if num // (2 ** bit_place):
            btis6[i] = num // (2 ** bit_place)
            num -= (2 ** bit_place)
        bit_place -= 1
        i+=1
    return btis6

def bits24_to_nums(bits24):
    bit_place = 7
    num = 0
    result = []
    for bit in bits24:
        if bit_place < 0 :
            result.append(num)
            num = 0
            bit_place = 7
        if bit==1:
            num += (bit+1)**(bit_place)
        bit_place-=1
    else:
        result.append(num)

    return result



for t in range(1,int(input())+1):
    words = input()

    splited =splited_words_by4()
    splited_nums_by4 = decoding_4words(splited)

    splited_nums_by_24bits = []
    for nums4 in splited_nums_by4:
        tmp = []
        for num in nums4:
            tmp.extend(num_to_6bits(num))
        splited_nums_by_24bits.append(tmp)


    splited_24bits_by_nums=[]
    for bits24 in splited_nums_by_24bits:
        splited_24bits_by_nums.extend(bits24_to_nums(bits24))

    # print를 통해 어떻게 변환되고 싶으면 밑의 print 주석 실행

    # print(splited)
    # print(decoding_4words(splited))
    # print(splited_nums_by_24bits)
    # print(splited_24bits_by_nums)

    result = ''
    for num in splited_24bits_by_nums:
        result+=chr(num)
    # print(f'#{t} {result}')

    ans=''.join(list(map(chr,base64.b64decode(words))))
    print(f'#{t} {ans}')





