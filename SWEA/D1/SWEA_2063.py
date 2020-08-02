#중간값 찾기
import sys
sys.stdin = open("input.txt","r")
N = int(input())
print(sorted(list(map(int, input().split())))[N//2])