def solution(s):
    s = list(s)

    #이전이 숫자거나, 알파벳이면 True
    #공백이면 False
    flag = False
    for i in range(len(s)):


        if 97 <= ord(s[i]) <= 122 and flag == False:
            s[i] = chr(ord(s[i])-32)
            flag = True
            continue

        if 65 <= ord(s[i]) <= 90 and flag == True:
            s[i] = chr(ord(s[i])+32)
            flag = True
            continue

        if s[i] == ' ':
            flag = False
            continue
        flag = True

    return ''.join(s)

# print(solution("3people unFollowed me"))
# print(solution("aA3AApeople ASDASDSAD mQde"))
# print(solution(" A  sdf Frft "))
############################################################################################################
s = "3people unFollowed me"

answer = []
for i in range(len(s.split())):
    answer.append(s.split()[i][0].upper() + s.split()[i][1:].lower())
print(' '.join(answer))