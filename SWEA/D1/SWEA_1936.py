# 1대1 가위바위보
# 1 가위 2 바위 3 보
# 1 2 : 2
# 1 3 : 1
# 2 3 : 3
import sys
sys.stdin = open("input.txt","r")
a,b=map(int,input().split())
if a == 1:
    if b == 3:print('A')
    else:print('B')
if a == 2:
    if b == 1:print('A')
    else:print('B')
if a == 3:
    if b == 2:print('A')
    else:print('B')