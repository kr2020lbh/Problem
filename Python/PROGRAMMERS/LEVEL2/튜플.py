def solution(s):
    answer = []
    dp = [0]*(100001)
    for ele in s[1:len(s)-1]:
        if ele == '{':
            num = ''

        elif ele == '}':
            for i in list(map(int,num.split(','))):
                dp[i] += 1
        else:
            num+=ele

    for i in (sorted(enumerate(dp),key=lambda x:-x[1])):
        if i[1] == 0:
            break
        answer.append(i[0])

    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")