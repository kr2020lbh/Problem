import sys
sys.stdin = open("input.txt","r")
import re
p = re.compile('.*FBI.*')
flag = False
for _ in range(5):
    FBI = input()
    if p.match(FBI):
        flag = True
        print(_ + 1,end=' ')
if not flag:
    print("HE GOT AWAY!")