import sys
sys.stdin = open("test.txt")

test_case = int(input())
for tc in range(1, test_case + 1):
    given_string = input()
    stack = []
    flag = 0
    for char in given_string:
        if len(stack) == 0:
            stack.append(char)
        else:
            if stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

    print(f'#{tc} {len(stack)}')

