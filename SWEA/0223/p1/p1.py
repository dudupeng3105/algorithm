import sys

sys.stdin = open("test.txt")

test_case = int(input())
for tc in range(1, test_case + 1):
    given_string = input()
    stack = []
    print(f'#{tc}', end=" ")
    for char in given_string:
        if char in ['*', '/', '-', '+']:
            stack.append(char)
        else:
            print(f"{char}", end="")
    while stack:
        print(stack.pop(), end="")
    print()