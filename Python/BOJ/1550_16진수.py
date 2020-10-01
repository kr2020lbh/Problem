#0-9 A-F
num = input()
numbers = '0123456789'
alphabets = ['A','B','C','D','E','F']
my_num = num[::-1]
res = 0
for i in range(len(my_num)):
    n = my_num[i]
    if n in numbers:res+=int(n)*16**i
    else:res+=(alphabets.index(n)+10)*16**i
print(res)


