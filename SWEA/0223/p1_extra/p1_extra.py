import sys

sys.stdin = open("test.txt")

test_case = int(input())

for tc in range(1, test_case + 1):
    stack = []  # 스택
    res = ''  # 출력
    given_string = input()
    for x in given_string:
        if x not in ['(', ')', '+', '/', '-', '*']:
            res += x
        else:
            # 스택에 들어올 연산자의 우선순위가 스택의 탑에 있는 연산자의 우선순위보다 높을 떄 삽입됨
            if x == '(':
                stack.append(x)
            # *와 /는 우선순위가 같으므로 넣을 때 탑에 * / 가 있으면 빼버림
            elif x == '*' or x == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    res += stack.pop()
                stack.append(x)
            # 스택에 +-*/ 와 상관없이 있는 연산자 다 빼버림 ( 만나는 거 아니면
            elif x == '+' or x == '-':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.append(x)
            elif x == ')':  # 스택에서 ( 만날 때까지 빼고, (도 뺌, )는 넣지도 않음
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.pop()

    while stack:
        res += stack.pop()
    print(res)
