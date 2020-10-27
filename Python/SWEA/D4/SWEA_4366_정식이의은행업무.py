import sys
sys.stdin =open("input.txt","r")
def find_res(b_n,t_n):
    for i in range(41):
        for j in range(41):
            if b_n + 2**i == t_n + 3**j or \
                    b_n + 2**i == t_n - 3**j or \
                    b_n + 2**i == t_n + 2*3**j or \
                    b_n + 2**i == t_n - 2*3**j: return b_n + 2**i

            if b_n - 2**i == t_n + 3**j or \
                    b_n - 2**i == t_n - 3**j or \
                    b_n - 2**i == t_n + 2*3**j or \
                    b_n - 2**i == t_n - 2*3**j:return b_n - 2**i

for t in range(1,int(input())+1):
    binary_input = input()
    b_n = int(binary_input,2)
    ternary_input = input()
    ternary_input = ternary_input[::-1]
    t_n = 0
    for i in range(len(ternary_input)):
        t_n+=int(ternary_input[i])*3**i
    print("#{} {}".format(t,find_res(b_n,t_n)))
for i in range(1,10):
    print(2^i)
