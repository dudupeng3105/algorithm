import sys


def dfs(elements, depth, temp):
    global minimum_sum

    # 백 트래킹 조건
    if depth > n:
        return
    if temp >= minimum_sum:  # 중간이라도 크면 바로 나감
        return
    if depth == n:  # 숫자가 5개 모였고, temp가 미니멈 보다 작음
        minimum_sum = temp
        return

    for i in elements:  # 0, 1, 2  # i == 1
        next_elements = elements[:] # 0, 1, 2
        next_elements.remove(i) # 0, 2
        dfs(next_elements, depth+1, temp+arr[depth][i])
        # depth 를 row 봐도 됨
    return


sys.stdin = open("test.txt")
test_case = int(input())

for tc in range(1, test_case + 1):
    n = int(input())
    arr = [[0 for _ in range(n)] for __ in range(n)]

    for i in range(n):
        arr[i] = list(map(int, input().split()))

    element = [x for x in range(n)]
    minimum_sum = 1000000
    dfs(element, 0, 0)
    print(f'#{tc} {minimum_sum}')