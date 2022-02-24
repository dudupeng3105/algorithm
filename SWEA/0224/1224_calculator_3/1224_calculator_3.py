import sys


# 연산 함수
def calculator_operation(opreation, num1, num2):
    if opreation == '*':
        return num2 * num1
    elif opreation == '+':
        return num2 + num1
    elif opreation == '-':
        return num2 - num1
    else:  # /
        return num2 // num1


sys.stdin = open("test.txt")

for tc in range(1, 11):
    stack = []  # 스택
    result = []  # 출력
    length = int(input())
    given_string = input()
    for x in given_string:
        if x not in ['(', ')', '+', '/', '-', '*']:
            int_x = int(x)
            result.append(int_x)
        else:
            # 스택에 들어올 연산자의 우선순위가 스택의 탑에 있는 연산자의 우선순위보다 높을 떄 삽입됨
            if x == '(':
                stack.append(x)
            # *와 /는 우선순위가 같으므로 넣을 때 탑에 * / 가 있으면 빼버림
            elif x == '*' or x == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    op = stack.pop()
                    a1 = result.pop()
                    a2 = result.pop()
                    result.append(calculator_operation(op, a1, a2))
                stack.append(x)
            # 스택에 +-*/ 와 상관없이 있는 연산자 다 빼버림 ( 만나는 거 아니면
            elif x == '+' or x == '-':
                while stack and stack[-1] != '(':
                    op = stack.pop()
                    a1 = result.pop()
                    a2 = result.pop()
                    result.append(calculator_operation(op, a1, a2))
                stack.append(x)
            elif x == ')':  # 스택에서 ( 만날 때까지 빼고, (도 뺌, )는 넣지도 않음
                while stack and stack[-1] != '(':
                    op = stack.pop()
                    a1 = result.pop()
                    a2 = result.pop()
                    result.append(calculator_operation(op, a1, a2))
                stack.pop()

    while stack:
        op = stack.pop()
        a1 = result.pop()
        a2 = result.pop()
        result.append(calculator_operation(op, a1, a2))
    print(f'#{tc} {result[0]}')

