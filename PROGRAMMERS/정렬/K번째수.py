def solution(array, commands):
    answer = []
    for command in commands:
        start = command[0]-1
        end = command[1]    
        select = command[2]-1
        answer.append(sorted(array[start:end])[select])
    return answer