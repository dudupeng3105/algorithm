import sys
sys.stdin = open("test.txt")

test_case = int(input())
for tc in range(1, test_case + 1):
    given_string = input()
    stack = []
    flag = 0
    for char in given_string:
        if char == '{' or char == '(':
            stack.append(char)

        elif char == '}' or char == ')':
            if len(stack) == 0:
                flag = 1
                break
            else:
                top_char = stack.pop()
                if char == '}':
                    if top_char != '{':  # 짝이 다르면 안됨
                        flag = 1
                        break

                else:  # )
                    if top_char != '(':  # 짝이 다르면 안됨
                        flag = 1
                        break

    if flag or len(stack):
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')