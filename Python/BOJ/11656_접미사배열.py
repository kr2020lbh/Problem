import sys
sys.stdin = open("input.txt","r")
word = input()
[print(r) for r in sorted([ word[i:] for i in range(len(word))])]