import sys

sys.stdin = open("test.txt")
test_case = int(input())
for tc in range(1, test_case+1):
    given_string = list(input().split())
    result = []
    flag = 0
    for x in given_string:
        if x not in ['+', '*', '-', '/','.']:
            int_x = int(x)
            result.append(int_x)
        else:
            if x == '.':
                flag = 1
                break
            elif x == '*':
                if len(result) < 2:  # 피연산자 하나거나 없음
                    print(f'#{tc} error')
                    break
                else:
                    a1 = result.pop()
                    a2 = result.pop()
                    result.append(a1 * a2)

            elif x == '/':
                if len(result) < 2:  # 피연산자 하나거나 없음
                    print(f'#{tc} error')
                    break
                else:
                    a1 = result.pop()
                    a2 = result.pop()
                    result.append(a2 // a1)

            elif x == '-':
                if len(result) < 2:  # 피연산자 하나거나 없음
                    print(f'#{tc} error')
                    break
                else:
                    a1 = result.pop()
                    a2 = result.pop()
                    result.append(a2 - a1)

            elif x == '+':
                if len(result) < 2:  # 피연산자 하나거나 없음
                    print(f'#{tc} error')
                    break
                else:
                    a1 = result.pop()
                    a2 = result.pop()
                    result.append(a1 + a2)

    if flag:
        if len(result) > 1:  # 남아있는 숫자가 2개 이상
            print(f'#{tc} error')
        else:
            print(f'#{tc} {result[0]}')
