def solution(clothes):
    cloth_dict = {}
    for cloth in clothes:
        if cloth_dict.get(cloth[1]):
            cloth_dict[cloth[1]].append(cloth[0])
        else:
            cloth_dict[cloth[1]]=[cloth[0]]
    answer = 1
    for c in cloth_dict.values():
        answer*=(len(c)+1)
    return answer-1

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]


from collections import Counter
answer = 1
for cnt in Counter([c_type for c_name, c_type in clothes]).values():
    answer *= (cnt + 1)
print(answer-1)