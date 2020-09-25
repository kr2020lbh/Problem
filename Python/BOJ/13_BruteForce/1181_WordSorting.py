import sys
sys.stdin = open("input.txt","r")
N = int(input())
words = []
for i in range(N):
    word = input()
    words.append(word)
words=set(words)
result = sorted(words,key=lambda x:(len(x),x))
for i in range(len(result)):
    print(result[i])
