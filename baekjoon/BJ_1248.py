import sys


def dfs(depth):
    if depth == 0:
        pass

    else:
        sign_num = depth - 1

        for i in range(depth):
            if sign[sign_num] == '+':
                if sum(result[i: depth]) <= 0:  # 조건 안맞으면 백
                    return
            elif sign[sign_num] == '-':
                if sum(result[i: depth]) >= 0:  # 조건 안맞으면 백
                    return

            else:  # = 0
                if sum(result[i: depth]) != 0:  # 조건 안맞으면 백
                    return

            sign_num = sign_num + (N - i - 1)

        if depth == N:
            print(*result)
            exit(0)

    for i in range(-10, 11, 1):
        result.append(i)
        dfs(depth + 1)
        result.pop()


N = int(sys.stdin.readline())
sign = sys.stdin.readline().rstrip()
result = []
dfs(0)


# python은 시간초과
# pypy3은 통과
