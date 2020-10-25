from collections import Counter

def cut(cut_len,s):
    tmp = []
    for i in range(0,len(s),cut_len):
        tmp.append(''.join(s[i:i+cut_len]))
    idx = 0
    res = ''
    while idx < len(tmp):
        cnt = 1
        for i in range(idx+1,len(tmp)):

            if tmp[idx] == tmp[i]:
                cnt += 1
            else:
                break
        if cnt != 1:
            res += str(cnt) + tmp[idx]
        else:
            res += tmp[idx]
        idx = idx + cnt
    return len(res)



def solution(s):
    s = list(s)
    arr = [0] * 1001
    if len(s) == 1:
        return 1
    for i in range(len(s)//2,0,-1):
        arr[cut(i,s)] += 1
    for i in range(1001):
        if arr[i]:
            return i

print(solution('a'))