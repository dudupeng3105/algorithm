import sys
from collections import deque
# 키로거
input = sys.stdin.readline
# 커서를 중심으로 왼쪽, 오른쪽 큐로 나눔
tc = int(input())
for _ in range(tc):
    given_string = input().rstrip()
    left, right = deque(), deque()

    for char in given_string:
        if char == '<':
            if left:
                right.appendleft(left.pop())
        elif char == '>':
            if right:
                left.append(right.popleft())
        elif char == '-':
            if left:
                left.pop()

        else:  # 알파벳
            left.append(char)

    print(''.join(left), end="")
    print(''.join(right))