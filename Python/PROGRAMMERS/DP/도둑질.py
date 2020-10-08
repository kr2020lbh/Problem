def solution(money):
    length =len(money)
    dp1 = [0] * length
    dp2 = [0] * length

    dp1[0] = money[0]
    dp1[1] = money[0]

    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, length-1):
        dp1[i] = max(dp1[i-1], money[i]+dp1[i-2])

    for i in range(2, length):
        dp2[i] = max(dp2[i-1], money[i]+dp2[i-2])
    return max(dp1[-2], dp2[-1])

money = [5,6,5,3,5,4]
print(solution(money))
