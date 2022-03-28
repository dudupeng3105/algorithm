from collections import deque
import sys

input = sys.stdin.readline


def operation(num, a):
    if a == '+':  # +
        return num + num
    elif a == '*':  # *
        return num * num
    else:  # a = 3  # /
        return 1


def bfs(num, op):
    q = deque()
    q.append((num, op))
    if num == e:
        return op
    while q:
        pre_num, op = q.popleft()
        for next_op in ['*', '+']:
            next_num = operation(pre_num, next_op)
            if next_num > e:
                continue
            else:
                if next_op == '*' and pre_num == 1:
                    continue
                if next_num == e:
                    return op + next_op
                q.append((next_num, op + next_op))

    return


s, e = map(int, input().split())
result = []
if s == e:
    print(0)
else:
    for op in ['*', '+', '/']:
        result.append(bfs(operation(s, op), op))
    min_op = -1
    # 가장 짧은 연산 찾기

    for r in result:
        if r:
            if min_op == -1:
                min_op = r
            else:
                if len(r) < len(min_op):
                    min_op = r
        else:
            continue

    print(min_op)

