word = input()
alphabet = dict()
for i in range(65,91):
    alphabet[chr(i)]=0

for w in word:
    alphabet[w] += 1
odd_even = [[],[]]
for key,value in alphabet.items():
    if value != 0:
        if value % 2:
            odd_even[1].append([key,value])
        else:
            odd_even[0].append([key,value//2])

ans = ''
if len(word)%2:#홀수길이
    if len(odd_even[1]) != 1:
        ans = "I'm Sorry Hansoo"
    else:
        _char, _cnt = odd_even[1][0]
        if _cnt > 1:
            flag = True
            for char,cnt in odd_even[0]:
                if flag==True and _char < char:
                    ans += _char * ((_cnt-1)//2)
                    flag = False
                ans += char*cnt
            if flag:
                ans = ans + _char*_cnt + ans[::-1]
            else:
                ans = ans + _char + ans[::-1]
        else:
            for char,cnt in odd_even[0]:
                ans += char*cnt
            ans = ans + _char + ans[::-1]

else:
    if len(odd_even[1]) != 0:
        ans = "I'm Sorry Hansoo"
    else:
        for char, cnt in odd_even[0]:
            ans += char*cnt
        ans += ans[::-1]
print(ans)
