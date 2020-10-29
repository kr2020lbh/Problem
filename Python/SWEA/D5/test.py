
def decode_binary(first_idx, second_idx, third_idx, fourth_idx):
    min_len = min((second_idx - first_idx), (third_idx -second_idx), (fourth_idx - third_idx))
    tmp_code = ((second_idx - first_idx) // min_len, (third_idx - second_idx) // min_len, (fourth_idx -third_idx) // min_len)
    print(tmp_code) 

codes = ['111100110','1100110','011110011','001100110']
for b_code in codes:
    first = second = third = False
    for i in range(len(b_code)):
        if first:
            if second:
                if third:
                    if b_code[i] == '0':
                        decode_binary(first_idx,second_idx,third_idx,i)
                        first = second = third = False
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

print(ord('A'))
print(ord('a'))