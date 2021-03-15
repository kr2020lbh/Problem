import sys
sys.stdin = open("input.txt","r")

string = list(map(lambda x:(ord(x[1]),x[0]),enumerate(input())))
ans = [''] * len(string)


for i in range(len(string)):
    min_idx = 0
    tmp = 'Z' * len(string)
    for j in range(len(string)):
        val,idx = string[j]
        tmp_ans = ans[::]
        tmp_ans[idx] = chr(val)
        if ''.join(tmp_ans) < tmp:
            tmp = ''.join(tmp_ans)
            min_idx = j
    ans[string[min_idx][1]] =chr(string[min_idx][0])
    string.pop(min_idx)
    print(''.join(ans))
