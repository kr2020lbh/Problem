import sys
sys.stdin = open("input.txt","r")

N = int(input())
for i in range(N):
    signals = input()

    if len(signals) == 1 or len(signals) == 3:
        print('NO')
        continue

    start = 0
    flag = True
    while start < len(signals):

        if signals[start] == '0':
            if start + 1 < len(signals):
                if signals[start+1] == '1':
                    start += 2
                    continue
            print('NO')
            flag = False
            break
        else:
            if start + 3 < len(signals):
                if signals[start+1] == '0':
                    if signals[start+2] == '0':
                        idx = start + 3
                        while idx < len(signals):
                            if signals[idx] == '1':
                                break
                            idx += 1
                        if idx < len(signals):
                            while idx < len(signals):
                                if signals[idx] == '0':
                                    break
                                idx += 1
                            start = idx
                            continue
            print('NO')
            flag = False
            break
    if flag:
        print('YES')


