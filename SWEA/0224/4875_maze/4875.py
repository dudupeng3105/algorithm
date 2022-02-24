import sys


def dfs(row, col):
    global ans
    # 백 트래킹 조건
    if row == end[0] and col == end[1]:
        ans = 1
        return

    for i in range(4):
        new_r, new_c = row + dr[i], col + dc[i]
        # 범위 안, 벽 아니고, 방문한적없고, 그리고 답 나왔으면 더 이상 안감
        if (0 <= new_r < n and 0 <= new_c < n) and arr[new_r][new_c] != '1' and \
                truth_map[new_r][new_c] == False and ans != 1:
            truth_map[new_r][new_c] = True
            dfs(new_r, new_c)

    return


sys.stdin = open("test.txt")
test_case = int(input())
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for tc in range(1, test_case + 1):
    n = int(input())
    arr = ['' for _ in range(n)]
    truth_map = [[False for _ in range(n)] for __ in range(n)]
    for i in range(n):
        arr[i] = input().rstrip()
    print(arr)
    # 2와 3의 위치 찾기
    start = [0, 0]
    end = [0, 0]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':
                start = [i, j]
            elif arr[i][j] == '3':
                end = [i, j]

    truth_map[start[0]][start[1]] = True
    ans = 0
    dfs(start[0], start[1])
    print(f'#{tc} {ans}')





