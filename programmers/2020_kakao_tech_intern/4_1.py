from collections import deque

board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
N = len(board)




def bfs():
    def move(old_r, old_c, old_type):
        if not old_type:  # type 0(가로)
            for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # 상 하 좌 우
                new_r, new_c = old_r + dr, old_c + dc
                if 0 <= new_c < N - 1 and 0 <= new_r < N:  # [new_x, new_y][new_x + 1, new_y]
                    if board[new_r][new_c] or board[new_r][new_c + 1]:
                        continue
                    else:
                        # 방문 및 거리(시간) 업데이트
                        if time_map[old_r][old_c][old_type] + 1 < time_map[new_r][new_c][old_type]:
                            time_map[new_r][new_c][old_type] = time_map[old_r][old_c][old_type] + 1
                            q.append((new_r, new_c, old_type))

        else:  # type 1(세로)
            for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # 상 하 좌 우
                new_r, new_c = old_r + dr, old_c + dc
                if 0 <= new_c < N and 0 <= new_r < N - 1:  # [new_x, new_y][new_x, new_y + 1]
                    # print("new_x, new_y", new_x, new_y)
                    if board[new_r][new_c] or board[new_r + 1][new_c]:
                        continue
                    else:
                        # 방문 및 거리(시간) 업데이트
                        if time_map[old_r][old_c][old_type] + 1 < time_map[new_r][new_c][old_type]:
                            time_map[new_r][new_c][old_type] = time_map[old_r][old_c][old_type] + 1
                            q.append((new_r, new_c, old_type))

    def rotate(old_r, old_c, old_type):
        if not old_type:  # 가로 type == 0
            # 왼쪽 점 기준
            if old_r != N - 1:  # 맨 아래줄만 아니면 시계방향으로 돌 수 있음
                if not board[old_r + 1][old_c] and not board[old_r + 1][old_c + 1]:
                    new_r, new_c, new_type = old_r, old_c, 1
                    if time_map[old_r][old_c][old_type] + 1 < time_map[new_r][new_c][new_type]:
                        time_map[new_r][new_c][new_type] = time_map[old_r][old_c][old_type] + 1
                        q.append((new_r, new_c, new_type))

            if old_r != 0:  # 맨 위줄만 아니면 반시계방향으로 돌 수 있음
                if not board[old_r - 1][old_c] and not board[old_r - 1][old_c + 1]:
                    new_r, new_c, new_type = old_r - 1, old_c, 1
                    if time_map[old_r][old_c][old_type] + 1 < time_map[new_r][new_c][new_type]:
                        time_map[new_r][new_c][new_type] = time_map[old_r][old_c][old_type] + 1
                        q.append((new_r, new_c, new_type))

            # 오른쪽 점 기준
            if old_r != N - 1:  # 맨 아래줄만 아니면 반시계방향으로 돌 수 있음
                if not board[old_r + 1][old_c] and not board[old_r + 1][old_c + 1]:
                    new_r, new_c, new_type = old_r, old_c + 1, 1
                    if time_map[old_r][old_c][old_type] + 1 < time_map[new_r][new_c][new_type]:
                        time_map[new_r][new_c][new_type] = time_map[old_r][old_c][old_type] + 1
                        q.append((new_r, new_c, new_type))

            if old_r != 0:  # 맨 위줄만 아니면 시시계방향으로 돌 수 있음
                if not board[old_r - 1][old_c] and not board[old_c - 1][old_c + 1]:
                    new_r, new_c, new_type = old_r - 1, old_c + 1, 1
                    if time_map[old_r][old_c][old_type] + 1 < time_map[new_r][new_c][new_type]:
                        time_map[new_r][new_c][new_type] = time_map[old_r][old_c][old_type] + 1
                        q.append((new_r, new_c, new_type))

        else:  # 세로 type == 1
            # 위 점 기준(표준)
            if old_c != N - 1:  # 맨 오른줄만 아니면 반시계방향으로 돌 수 있음
                # print("얍", old_r, old_c)
                if not board[old_r][old_c + 1] and not board[old_r + 1][old_c + 1]:
                    new_r, new_c, new_type = old_r, old_c, 0
                    if time_map[old_r][old_c][old_type] + 1 < time_map[new_r][new_c][new_type]:
                        time_map[new_r][new_c][new_type] = time_map[old_r][old_c][old_type] + 1
                        q.append((new_r, new_c, new_type))

            if old_c != 0:  # 맨 왼쪽만 아니면 시계방향으로 돌 수 있음
                if not board[old_r][old_c - 1] and not board[old_r + 1][old_c - 1]:
                    new_r, new_c, new_type = old_r, old_c - 1, 0
                    if time_map[old_r][old_c][old_type] + 1 < time_map[new_r][new_c][new_type]:
                        time_map[new_r][new_c][new_type] = time_map[old_r][old_c][old_type] + 1
                        q.append((new_r, new_c, new_type))

            # 아래 점 기준
            if old_c != N - 1:  # 맨 오른줄만 아니면 시계방향으로 돌 수 있음
                if not board[old_r][old_c + 1] and not board[old_r + 1][old_c + 1]:
                    new_r, new_c, new_type = old_r + 1, old_c, 0
                    if time_map[old_r][old_c][old_type] + 1 < time_map[new_r][new_c][new_type]:
                        time_map[new_r][new_c][new_type] = time_map[old_r][old_c][old_type] + 1
                        q.append((new_r, new_c, new_type))

            if old_c != 0:  # 맨 왼쪽만 아니면 반시계방향으로 돌 수 있음
                if not board[old_r][old_c - 1] and not board[old_r + 1][old_c - 1]:
                    new_r, new_c, new_type = old_r + 1, old_c - 1, 0
                    if time_map[old_r][old_c][old_type] + 1 < time_map[new_r][new_c][new_type]:
                        time_map[new_r][new_c][new_type] = time_map[old_r][old_c][old_type] + 1
                        q.append((new_r, new_c, new_type))
    time_map[0][0] = [0, 0]
    while q:

        r, c, type_num = q.popleft()
        #print("시작", r, c, type_num)
        # 상 하 좌 우
        move(r, c, type_num)
        # 축1, 축2 * 시계, 반시계
        rotate(r, c, type_num)


time_map = [[[99999, 99999] for _ in range(N)] for __ in range(N)]  # [가로, 세로]
q = deque()
q.append((0, 0, 0))
bfs()  # type 0(가로), type 1(세로)
print(min(time_map[N - 2][N - 1][1], time_map[N - 1][N - 2][0]))