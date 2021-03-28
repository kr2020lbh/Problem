import sys
sys.stdin = open("input.txt","r")

num = 2000000
arr = [False, False] + [True for _ in range(num - 1)]
primes = []
for i in range(2, num + 1):
    if arr[i]:
        primes.append(i)
        for j in range(i + i, num, i):
            arr[j] = False


def isPrime(n):
    if n > num:
        for prime in primes:
            if prime >= n:
                break
            elif n % prime == 0:
                return False
        return True

    else:
        return arr[n]


T = int(input())
for _ in range(T):
    s = sum(list(map(int,input().split())))
    if s < 4:
        print("NO")
    elif s % 2 == 0:
        print("YES")
    else:
        if isPrime(s-2):
            print("YES")
        else:
            print("NO")