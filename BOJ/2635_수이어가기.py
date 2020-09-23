def f(n):
    MAX = 0
    for i in range(n+1):
        res = [n]
        num = i
        before = n
        while True:
            res.append(num)
            if before-num < 0:break
            else:before,num = num,before-num

        if len(res)>MAX:
            MAX = len(res)
            RES = res[::]
    return MAX,RES


n = int(input())


MAX,RES = f(n)
print(MAX)
[print(num,end=' ') for num in RES]