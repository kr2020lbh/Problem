
def primes(n):
    #[ 0 1 2 3 4 5 6 ... n ]
    #[ f f ...             ]
    nums = [False, False] + [True] * (n-1)
    for idx, num in enumerate(nums):
        if num:
            k = idx * 2
            while k <= n:
                nums[k] = False
                k += idx

    result = ''
    for x,y in enumerate(nums):
        if y:
            result+=str(x)+' '
    return result

print(primes(1000000))

