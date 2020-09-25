#알파벳을 숫자로 변환
import sys
sys.stdin = open("input.txt","r")
[print(ord(char.upper())-64,end=' ') for char in input()]

