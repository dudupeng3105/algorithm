# 괄호변환

def solution(p):
    if not p:
        return ''
    print("p:", p)
    # 올바른 괄호 문자열 테스트
    test = []
    for char in p:
        if char == '(':
            test.append('(')
        else:
            if test:
                test.pop()
    if not test:
        return p

    stack = [p[0]]
    for i in range(1, len(p)):
        if not stack:
            break

        char = p[i]
        if char == '(':
            if stack[-1] == ')':
                stack.pop()
            else:
                stack.append('(')
        else:
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')

    if not stack and i == len(p)-1:
        u = p[:i+1]
        v = ''
    else:
        u = p[:i]
        v = p[i:]
    print("u", "v", u, v)
    # 올바른 괄호 문자열 테스트
    test = []
    for char in u:
        if char == '(':
            test.append('(')
        else:
            if test:
                test.pop()


    # 올바른 괄호 문자열(짝도 맞음)
    answer = ''
    if not test:
        answer = u + solution(v)
    else:
        temp = '(' + solution(v) + ')'
        for char in u[1:-1]:
            if char == '(':
                temp += ')'
            else:
                temp += '('
        answer = temp

    return answer

input_value = "(()())()"
print(solution(input_value))