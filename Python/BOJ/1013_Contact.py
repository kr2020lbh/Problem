import sys
import re
sys.stdin = open("input.txt","r")

N = int(input())
p = re.compile('(100+1+|01)+')
[print("YES") if p.fullmatch(input()) else print("NO") for _ in range(N)]