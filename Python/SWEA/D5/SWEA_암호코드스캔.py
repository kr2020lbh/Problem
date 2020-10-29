import sys
sys.stdin =open("input.txt","r")
code = {(2, 1, 1): '0',(2, 2, 1): '1',(1, 2, 2): '2',(4, 1, 1): '3',(1, 3, 2): '4',(2, 3, 1): '5',(1, 1, 4): '6',(3, 1, 2): '7',(2, 1, 3): '8',(1, 1, 2): '9'}
hexa_to_bin = {'0':'0000', '1':'0001', '2':'0010', '3':'0011','4':'0100', '5':'0101', '6':'0110', '7':'0111','8':'1000', '9':'1001', 'A':'1010', 'B':'1011','C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}


def check(number):
    odd_sum = 0
    even_sum = 0
    for i in range(len(number)):
        if i%2==0:
            odd_sum+=int(number[i])
        else:
            even_sum+=int(number[i])
    result = odd_sum*3 + even_sum
    if result % 10==0:
        return odd_sum+even_sum
    else:
        return False


def get_binary_from_hexa(hexa_code):
    b_code = ''
    for hexa in hexa_code:
        b_code += hexa_to_bin[hexa]
    return b_code


def decode_binary(first_idx, second_idx, third_idx, fourth_idx):
    min_len = min((second_idx - first_idx), (third_idx -second_idx), (fourth_idx - third_idx))
    tmp_code = ((second_idx - first_idx) // min_len, (third_idx - second_idx) // min_len, (fourth_idx -third_idx) // min_len)
    return code[tmp_code]


for t in range(int(input())):
    N,M = map(int,input().split())
    arr = [input() for _ in range(N)]
    decode_number_set = set()
    for _ in range(N):
        hexa_code = arr[_]
        b_code = get_binary_from_hexa(hexa_code)

        first = second = third = False
        decode_numbers = ''
        for i in range(len(b_code)):
            if first:
                if second:
                    if third:
                        if b_code[i] == '0':
                            first = second = third = False
                            decode_number = decode_binary(first_idx, second_idx, third_idx, i)
                            decode_numbers += decode_number
                            if len(decode_numbers) == 8:
                                decode_number_set.add(decode_numbers)
                                decode_numbers=''
                    else:
                        if b_code[i] == '1':
                            third = True
                            third_idx = i
                else:
                    if b_code[i] == '0':
                        second = True
                        second_idx = i
            else:
                if b_code[i] == '1':
                    first = True
                    first_idx = i

    test_result = 0
    for numbers in decode_number_set:
        check_result = check(numbers)
        if check_result:
            test_result+=check_result

    print("#{} {}".format(t+1,test_result))