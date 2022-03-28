from collections import defaultdict


def operation(a, op, b):
    if op == '+':
        return a + b
    elif op == '*':
        return a * b
    else:  # -
        return a - b


def dfs(r, c, path):
    global ans

    truth_map[r][c] = True
    if r == n - 1 and c == n - 1:
        # 연산
        temp = int(path[0])
        i = 1
        while i < len(path):
            if path[i] in ['+', '*', '-']:
                temp = operation(temp, path[i], int(path[i + 1]))
                i += 2
            else:
                i += 1

        ans.append(temp)  # 담아두고 밖에서 최소값 최대값 출력할거임

    for dr, dc in [(1, 0), (0, 1)]:
        n_r, n_c = r + dr, c + dc
        if 0 <= n_r < n and 0 <= n_c < n:
            if not truth_map[n_r][n_c]:
                dfs(n_r, n_c, path + arr[n_r][n_c])
                truth_map[n_r][n_c] = False

    return


# input 받기
n = int(input())
arr = [['' for _ in range(n)] for __ in range(n)]
for i in range(n):
    arr[i] = list(input().split())

truth_map = [[False for _ in range(n)] for __ in range(n)]
ans = []
dfs(0, 0, arr[0][0])
print(max(ans), min(ans))