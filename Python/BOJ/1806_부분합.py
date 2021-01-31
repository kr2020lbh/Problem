import sys
sys.stdin = open("input.txt","r")

# N,S = map(int,input().split())
# numbers = list(map(int,input().split()))

# def sol():
#     length = len(numbers)
#     for window_length in range(1,length+1):
#         if window_length != 1:
#             start_idx = 0
#             sumation = sum(numbers[start_idx:window_length])
#             for end_idx_idx in range(window_length,length):
#                 if sumation >= S:
#                     return window_length
#                 else:
#                     sumation = sumation - numbers[start_idx] + numbers[end_idx_idx]
#                     start_idx+=1
#         else:
#             for i in range(length):
#                 if numbers[i] >= S:
#                     return window_length
#     else:
#         return 0
# sol()


def sol():
    answer = 1000001
    start_idx = 0
    end_idx = 1
    while start_idx != N:
        if sumation[end_idx] - sumation[start_idx] >= S:
            if end_idx - start_idx< answer:
                answer = end_idx - start_idx
            start_idx += 1
            
        else:
            if end_idx != N:
                end_idx += 1
            else:
                start_idx += 1
    if answer != 1000001:
        return answer
    return 0

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
sumation = [0] * (N + 1)
for i in range(1, N + 1):
    sumation[i] = sumation[i-1] + numbers[i-1]  
print(sol())