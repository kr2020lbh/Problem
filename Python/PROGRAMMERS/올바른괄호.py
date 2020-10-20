def solution(s):
    stack = []
    for bracket in s:
        if bracket == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                return False

    if stack:
        return False
    return True

print(solution("()()"))
print(solution("(())()"))
print(solution(")()())"))