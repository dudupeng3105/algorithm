from collections import deque


# displacement함수에 사용하기 위한 참조 테이블
def matching_table(direction):
    if direction == 1:  # 상+
        result = (-1, 0, [1, 2, 5, 6])
        return result
    elif direction == 2:  # 하
        result = (1, 0, [1, 2, 4, 7])
        return result
    elif direction == 3:  # 좌
        result = (0, -1, [1, 3, 4, 5])
        return result
    else:  # direction == 4:  우
        result = (0, 1, [1, 3, 6, 7])
        return result


# dr, dc, 매칭되는 터널 리스트 돌려줌
def displacement(tunnel_shape):
    if tunnel_shape == 1:  # 상하좌우(1234)
        d = [matching_table(1), matching_table(2), matching_table(3), matching_table(4)]
    elif tunnel_shape == 2:  # 상하(12)
        d = [matching_table(1), matching_table(2)]
    elif tunnel_shape == 3:  # 좌우(34)
        d = [matching_table(3), matching_table(4)]
    elif tunnel_shape == 4:  # 상우*(14)
        d = [matching_table(1), matching_table(4)]
    elif tunnel_shape == 5:  # 하우(24)
        d = [matching_table(2), matching_table(4)]
    elif tunnel_shape == 6:  # 하좌(23)
        d = [matching_table(2), matching_table(3)]
    else:  # 7 상좌(13)
        d = [matching_table(1), matching_table(3)]

    return d


def bfs():
    global cnt
    q = deque()
    q.append((s_r, s_c))  # r, c, time
    visited[s_r][s_c] = 1
    cnt += 1
    while q:
        r, c = q.popleft()
        current_shape = arr[r][c]
        d_r_c_matching = displacement(current_shape)
        for dr, dc, matching_tunnels in d_r_c_matching:
            n_r, n_c = r + dr, c + dc
            if 0 <= n_r < row and 0 <= n_c < col and visited[n_r][n_c] == 0 and visited[r][c] < l:
                next_shape = arr[n_r][n_c]
                if next_shape in matching_tunnels:
                    cnt += 1
                    visited[n_r][n_c] = visited[r][c] + 1
                    q.append((n_r, n_c))


# main
test_case = int(input())
for tc in range(1, test_case + 1):
    row, col, s_r, s_c, l = map(int, input().split())
    arr = [[0 for _ in range(col)] for __ in range(row)]
    for i in range(row):
        arr[i] = list(map(int, input().split()))

    visited = [[0 for _ in range(col)] for __ in range(row)]
    cnt = 0
    bfs()
    print(f'#{tc} {cnt}')
