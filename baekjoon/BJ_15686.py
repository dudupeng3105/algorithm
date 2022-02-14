import sys

n, m = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(n)] for __ in range(n)]
# 입력받기
for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().split()))

chicken_store = []
house_store = []
# 치킨집, 하우스 리스트 찾기
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken_store.append((i, j))
            arr[i][j] = 0  # 치킨집 일단 0 처리
        elif arr[i][j] == 1:
            house_store.append((i, j))

chicken_store_cnt = len(chicken_store)


# 그냥 좌표로 거리 구해버리기~
def calculate_temp(store_lst):
    result = 0

    for house in house_store:
        h_row, h_col = house
        min_dist = 10000000
        for store in store_lst:
            s_row, s_col = store
            temp = abs(h_row-s_row) + abs(h_col-s_col)
            if temp < min_dist:
                min_dist = temp

        result += min_dist

    return result

# 치킨집 조합 by dfs
def dfs(start, depth, m_lst):
    global result

    if depth == m:  # 치킨집 n개 일때
        result_temp = calculate_temp(m_lst)
        result = min(result, result_temp)

        return

    for i in range(start, chicken_store_cnt):
        m_lst.append(chicken_store[i])
        dfs(i + 1, depth + 1, m_lst)
        m_lst.pop()


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 10000000
dfs(0, 0, [])
print(result)



