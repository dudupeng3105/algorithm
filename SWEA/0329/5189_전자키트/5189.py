test_case = int(input())


def dfs(depth, elements):
    global ans
    if depth == n - 1:
        print(elements)
        # 계산
        temp = arr[0][elements[0]]
        for i in range(n-2):
            temp += arr[elements[i]][elements[i+1]]
        temp += arr[elements[i+1]][0]

        if temp < ans:
            ans = temp
        return

    for next_element in range(1, n):
        if next_element not in elements:
            elements.append(next_element)
            dfs(depth + 1, elements)
            elements.pop()


for tc in range(1, test_case + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 9999999
    dfs(0, [])
    print(f'#{tc} {ans}')