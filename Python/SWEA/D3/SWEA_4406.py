import sys
sys.stdin = open('input.txt','r')

for t in range(1,int(input())+1):
    result = ''.join([word for word in input() if not word in ['a','e','i','o','u']])
    print(f'#{t} {result}')
