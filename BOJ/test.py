def f(N):
    if len(N) == 1:
        n = '0' + N
    else:
        n = str( int(N[0]) + int(N[1]) )

    return N[-1]+n[-1]

n = input()
tmp = f(n)
count = 1
while int(n) != int(tmp):
    tmp = f(tmp)
    count+=1
print(count)