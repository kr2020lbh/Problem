target = input()
bomb = input()
T = len(target)
B = len(bomb)
S= []
for i in range(T):
    S.append(target[i])
    if T>=B:
        if ''.join(S[len(S)-B:len(S)]) == bomb:
            [S.pop() for _ in range(B)]
if S:
    print(''.join(S))
else:
    print("FRULA")
