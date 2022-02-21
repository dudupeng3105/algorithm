import sys
sys.stdin = open("test.txt")

test_case = int(input())
for tc in range(1, test_case + 1):
    given_list = list(input())
    stack = list()
    flag = 0
    for char in given_list:
        if char == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                flag = 1
                break
            else:
                stack.pop()

    if flag or len(stack):
        print(f'#{tc} -1')
    else:
        print(f'#{tc} 1')
