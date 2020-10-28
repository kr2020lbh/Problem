import sys
sys.stdin =open("tt.txt","r")

def check(number):
    odd_sum = 0
    even_sum = 0
    for i in range(len(number)-1):
        if i%2==0:
            odd_sum+=int(number[i])
        else:
            even_sum+=int(number[i])
    result = odd_sum*3 + even_sum + int(number[-1])
    if result % 10==0:
        return int(number[-1])+odd_sum+even_sum
    else: return False

code = {}
for i in range(1,15):
    zero = '0'*i*3 + '1'*2*i + '0'*i + '1'*i
    one = '0'*i*2 + '1'*2*i + '0'*2*i + '1'*i
    two = '0'*i*2 + '1'*i*1 + '0'*i*2 + '1'*i*2
    three = '0'*i*1 +'1'*i*4 +'0'*i*1 +'1'*i*1
    four = '0'*i*1 +'1'*i*1 +'0'*i*3 +'1'*i*2
    five = '0'*i*1 +'1'*i*2 +'0'*i*3 +'1'*i*1
    six = '0'*i*1 +'1'*i*1 +'0'*i*1 +'1'*i*4
    seven = '0'*i*1 +'1'*i*3 +'0'*i*1 +'1'*i*2
    eight = '0'*i*1 +'1'*i*2 +'0'*i*1 +'1'*i*3
    nine = '0'*i*3 +'1'*i*1 +'0'*i*1 +'1'*i*2
    code[zero] = 0;code[one] = 1;code[two] = 2;code[three]=3;code[four]=4
    code[five]=5;code[six]=6;code[seven]=7;code[eight]=8;code[nine]=9




arr = [input()]
res_set = set()

for hexa_code in arr:
    hexa_code = hexa_code.rstrip('0')
    if len(hexa_code)==0:
        continue
    binary_code = ''
    for hexa in hexa_code:
        binary = str(bin(int(hexa,16)))[2::]
        binary_code += '0'*(4-len(binary))+binary
    sentence = binary_code + '0'

    cnt = 0
    first = second = third = False
    res = []
    for i in range(len(sentence)):
        if first:
            if second:
                if third:
                    if sentence[i] == '0':
                        res.append([first_idx,second_idx,third_idx,i-1])
                        first = second = third = False
                else:
                    if sentence[i] =='1':
                        third = True
                        third_idx = i
            else:
                if sentence[i] == '0':
                    second = True
                    second_idx = i
        else:
            if sentence[i] == '1':
                first = True
                first_idx = i

    eightofone = ''

    for r in res:
        tmp_code = sentence[r[0]:r[-1] + 1]
        min_len = min((r[1]-r[0]),(r[2]-r[1]),(r[3]+1-r[2]))
        while len(tmp_code) != min_len*7:
            tmp_code = '0' + tmp_code
        eightofone += str(code[tmp_code])
        if len(eightofone) == 8:
            res_set.add(eightofone)
            eightofone = ''
print(res_set)
test_result = 0
for numbers in res_set:
    check_result = check(numbers)
    if check_result:
        test_result+=check_result