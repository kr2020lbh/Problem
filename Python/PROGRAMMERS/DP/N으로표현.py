def check(N,number):
    dp = [set()]
    for i in range(1,9):
        dp.append(set())
        dp[i].add(int(str(N)*i))
    for i in range(1,9):
        for j in range(1,i+1):
            for num1 in dp[i]:
                for num2 in dp[j]:
                    dp[i+j].add(num1+num2)
                    dp[i+j].add(num1-num2)
                    dp[i+j].add(num2-num1)
                    dp[i+j].add(num1*num2)
                    if num2 != 0:
                        dp[i+j].add(num1//num2)
                    if num1 != 0:
                        dp[i+j].add(num2//num1)
            if i < j:
                if number in dp[i]:
                    return i
                if number in dp[j]:
                    return j
            else:
                if number in dp[j]:
                    return j
                if number in dp[i]:
                    return i
            if number in dp[i+j]:
                return i+j

    return False

def solution(N, number):
    if N == number:
        return 1
    res = check(N,number)
    if res:
        return res
    else:
        return -1
print(solution(4,17))