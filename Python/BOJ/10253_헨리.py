import sys
from fractions import Fraction
sys.stdin = open("input.txt","r")
def sol(a,b):
    if a == 1:
        print(b)
    else:
        i = b//a + 1
        tmp = Fraction(a,b) - Fraction(1,i)
        sol(tmp.numerator,tmp.denominator)

for _ in range(int(input())):
    a,b = map(int,input().split())
    sol(a,b)

