def solution(s):
    stack = []
    for char in s:
        if not stack:
            stack.append(char)
        else:
            if stack[-1] == char:
                stack.pop(-1)
            else:
                stack.append(char)
    if stack:
        return 0
    else:
        return 1

print(solution('baabbaab'))
print(solution('abaaba'))
print(solution('bbbaaaab'))