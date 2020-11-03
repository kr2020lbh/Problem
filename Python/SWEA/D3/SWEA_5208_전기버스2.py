import sys
sys.stdin = open("input.txt", "r")
for t in range(1,int(input())+1):
    tmp = list(map(int,input().split()))
    N = tmp[0]
    charger = [0] + tmp[1:]
    battery = charger[1]
    location = 1
    res = 0
    while True:
        if battery + location >= N:
            break
        else:
            MAX = 0
            for d_loc in range(location+1,location+1+battery):
                if d_loc + charger[d_loc] > MAX:
                    MAX = d_loc + charger[d_loc]
                    next_location = d_loc
            battery = charger[next_location]
            location = next_location
            res += 1
    print("#{} {}".format(t,res))