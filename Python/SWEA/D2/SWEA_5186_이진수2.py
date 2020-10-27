import sys
sys.stdin = open("input.txt", "r")

# for t in range(1,int(input())+1):
#     n = float(input())
#     ans = ''
#     for i in range(1,14):
#         if n == 0:break
#         if n >= 2**(-i):
#             n -= 2**(-i)
#             ans += '1'
#         else:
#             ans += '0'
#     else:
#         ans = 'overflow'
#     print('#{} {}'.format(t,ans))

for t in range(1,int(input())+1):
    n = float(input())
    ans=''
    while n!=0:
        if len(ans)>12:
            ans = 'overflow'
            break
        if n*2 >= 1:
            n=n*2-1
            ans += '1'
        else:
            n*=2
            ans += '0'
    print("#{} {}".format(t,ans))
