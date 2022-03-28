import itertools


def dfs(elements, start, depth):
    global result

    if depth == n:
        for combi in itertools.combinations(elements, n//2):
            c1 = list(combi)
            c2 = list(set(elements) - set(c1))
            a_taste = 0
            for x, y in itertools.combinations(c1, 2):
                a_taste += (arr[x][y] + arr[y][x])
            b_taste = 0
            for x_2, y_2 in itertools.combinations(c2, 2):
                b_taste += (arr[x_2][y_2] + arr[y_2][x_2])
            temp = abs(a_taste-b_taste)
            if temp < result:
                result = temp
        return

    for i in range(start, n):
        elements.append(i)
        dfs(elements, i + 1, depth + 1)
        elements.pop()


test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input())
    arr = [[0 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        arr[i] = list(map(int, input().split()))
    result = 99999999
    dfs([], 0, 0)
    print(f'#{tc} {result}')