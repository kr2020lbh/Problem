import sys
sys.stdin = open("input.txt","r")
def f():
    SUM = sum(heights) - 100
    for i in range(0, 8):
        find = SUM - heights[i]
        for j in range(i + 1, 9):
            if heights[j] == find:
                del heights[i]
                del heights[j-1]
                return

heights = [int(input()) for _ in range(9)]
f()
[print(n) for n in sorted(heights)]


