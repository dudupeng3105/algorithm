import sys
sys.stdin = open("test.txt")

for tc in range(1, 10 + 1):
    s1, s2 = map(int, input().split())
    n, given_string = s1, str(s2)
    stack = []
    flag = 0
    for char in given_string:
        if len(stack) == 0:
            if char != '0':
                stack.append(char)
        else:
            if stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

    print(f'#{tc}', ''.join(stack))