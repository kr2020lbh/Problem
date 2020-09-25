def solution(numbers):
    if not sum(numbers):
        return '0'
    return "".join(sorted(map(str, numbers), reverse=True, key=lambda x: x * 3))


numbers = [3, 30, 34, 5, 9]

print(sorted(map(str, numbers), reverse=True, key=lambda x: x * 3))
print()