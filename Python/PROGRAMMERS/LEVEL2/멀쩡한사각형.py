import math
def solution(w,h):
    return w*h-(w+h-math.gcd(w,h))

solution(2,2)

