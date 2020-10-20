def get_result(priority,n,expressions):
    if n == 2:
        return str(eval(expressions))
    if priority[n] == '*':
        result = eval('*'.join([get_result(priority,n+1,expression) for expression in expressions.split('*')]))
    if priority[n] == '+':
        result = eval('+'.join([get_result(priority,n+1,expression) for expression in expressions.split('+')]))
    if priority[n] == '-':
        result = eval('-'.join([get_result(priority,n+1,expression) for expression in expressions.split('-')]))
    return str(result)
def solution(expressions):
    answer = 0
    priorities = [['-','*','+'],['-','+','*'],
                ['+','*','-'],['+','-','*'],
                ['*','+','-'],['*','-','+']]
    for priority in priorities:
        answer = max(answer,abs(int((get_result(priority,0,expressions)))))
    return answer

solution("100-200*300-500+20*400+10")