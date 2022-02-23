import sys

sys.stdin = open("test.txt")

for tc in range(1, 11):
    stack = []  # 스택
    length = int(input())
    given_string = input()
    result = []
    for x in given_string:
        if x not in ['+', '*']:
            int_x = int(x)
            result.append(int_x)
        else:
            # 탑에 * 가 있으면 빼버리고 넣음
            if x == '*':
                while stack and stack[-1] == '*':
                    op = stack.pop() # 꼽하기 빼버림
                    a1 = result.pop()
                    a2 = result.pop()
                    result.append(a1*a2)
                stack.append(x)
            # 스택에 +* 와 상관없이 있는 연산자 다 빼버림 ( 만나는 거 아니면
            elif x == '+':
                while stack:
                    op = stack.pop()
                    if op == '*':
                        a1 = result.pop()
                        a2 = result.pop()
                        result.append(a1 * a2)
                    if op == '+':
                        a1 = result.pop()
                        a2 = result.pop()
                        result.append(a1 + a2)
                stack.append(x)

    while stack:
        op = stack.pop()
        if op == '*':
            a1 = result.pop()
            a2 = result.pop()
            result.append(a1 * a2)
        if op == '+':
            a1 = result.pop()
            a2 = result.pop()
            result.append(a1 + a2)

    print(f'#{tc} {result[0]}')