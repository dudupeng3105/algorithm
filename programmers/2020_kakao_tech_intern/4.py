from collections import deque

board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
N = len(board)


# 경우의 수
# 가로, 세로
# 상, 하, 좌, 우, 좌(아래), 우(위)
# 시계, 반시계

def move(old_x, old_y, old_type):
    if not old_type:  # type 0(가로)
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # 상 하 좌 우
            new_x, new_y = old_x + dx, old_y + dy
            if 0 <= new_x < N - 1 and 0 <= new_y < N:  # [new_x, new_y][new_x + 1, new_y]
                if board[new_y][new_x] or board[new_y][new_x + 1]:
                    continue
                else:
                    # 방문 및 거리(시간) 업데이트
                    if time_map[old_x][old_y][old_type] + 1 < time_map[new_x][new_y][old_type]:
                        time_map[new_x][new_y][old_type] = time_map[old_x][old_y][old_type] + 1
                        print("하이")
                        q.append((new_x, new_y, old_type))

    else:  # type 1(세로)
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # 상 하 좌 우
            new_x, new_y = old_x + dx, old_y + dy
            if 0 <= new_x < N and 0 <= new_y < N - 1:  # [new_x, new_y][new_x, new_y + 1]
                print("new_x, new_y", new_x, new_y)
                if board[new_y][new_x] or board[new_y + 1][new_x]:
                    continue
                else:
                    # 방문 및 거리(시간) 업데이트
                    if time_map[old_x][old_y][old_type] + 1 < time_map[new_x][new_y][old_type]:
                        time_map[new_x][new_y][old_type] = time_map[old_x][old_y][old_type] + 1
                        print("하이")
                        q.append((new_x, new_y, old_type))


def rotate(old_x, old_y, old_type):
    if not old_type:  # 가로 type == 0
        # 왼쪽 점 기준
        if old_y != N - 1:  # 맨 아래줄만 아니면 시계방향으로 돌 수 있음
            if not board[old_y + 1][old_x] and not board[old_y + 1][old_x + 1]:
                new_x, new_y, new_type = old_x, old_y, 1
                if time_map[old_x][old_y][new_type] + 1 < time_map[new_x][new_y][new_type]:
                    time_map[new_x][new_y][new_type] = time_map[old_x][old_y][new_type] + 1
                    q.append((new_x, new_y, new_type))

        if old_y != 0:  # 맨 위줄만 아니면 반시계방향으로 돌 수 있음
            if not board[old_y - 1][old_x] and not board[old_y - 1][old_x + 1]:
                new_x, new_y, new_type = old_x, old_y - 1, 1
                if time_map[old_x][old_y][new_type] + 1 < time_map[new_x][new_y][new_type]:
                    time_map[new_x][new_y][new_type] = time_map[old_x][old_y][new_type] + 1
                    q.append((new_x, new_y, new_type))

        # 오른쪽 점 기준
        if old_y != N - 1:  # 맨 아래줄만 아니면 반시계방향으로 돌 수 있음
            if not board[old_y + 1][old_x] and not board[old_y + 1][old_x + 1]:
                new_x, new_y, new_type = old_x + 1, old_y, 1
                if time_map[old_x][old_y][new_type] + 1 < time_map[new_x][new_y][new_type]:
                    time_map[new_x][new_y][new_type] = time_map[old_x][old_y][new_type] + 1
                    q.append((new_x, new_y, new_type))

        if old_y != 0:  # 맨 위줄만 아니면 시시계방향으로 돌 수 있음
            if not board[old_y - 1][old_x] and not board[old_y - 1][old_x + 1]:
                new_x, new_y, new_type = old_x + 1, old_y - 1, 1
                if time_map[old_x][old_y][new_type] + 1 < time_map[new_x][new_y][new_type]:
                    time_map[new_x][new_y][new_type] = time_map[old_x][old_y][new_type] + 1
                    q.append((new_x, new_y, new_type))

    else:  # 세로 type == 1
        # 위 점 기준(표준)
        if old_x != N - 1:  # 맨 오른줄만 아니면 반시계방향으로 돌 수 있음
            if not board[old_y][old_x + 1] and not board[old_y + 1][old_x + 1]:
                new_x, new_y, new_type = old_x, old_y, 0
                if time_map[old_x][old_y][new_type] + 1 < time_map[new_x][new_y][new_type]:
                    time_map[new_x][new_y][new_type] = time_map[old_x][old_y][new_type] + 1
                    q.append((new_x, new_y, new_type))

        if old_x != 0:  # 맨 왼쪽만 아니면 시계방향으로 돌 수 있음
            if not board[old_y][old_x - 1] and not board[old_y + 1][old_x - 1]:
                new_x, new_y, new_type = old_x - 1, old_y, 0
                if time_map[old_x][old_y][new_type] + 1 < time_map[new_x][new_y][new_type]:
                    time_map[new_x][new_y][new_type] = time_map[old_x][old_y][new_type] + 1
                    q.append((new_x, new_y, new_type))

        # 아래 점 기준
        if old_x != N - 1:  # 맨 오른줄만 아니면 시계방향으로 돌 수 있음
            if not board[old_y][old_x + 1] and not board[old_y + 1][old_x + 1]:
                new_x, new_y, new_type = old_x, old_y - 1, 0
                if time_map[old_x][old_y][new_type] + 1 < time_map[new_x][new_y][new_type]:
                    time_map[new_x][new_y][new_type] = time_map[old_x][old_y][new_type] + 1
                    q.append((new_x, new_y, new_type))

        if old_x != 0:  # 맨 왼쪽만 아니면 반시계방향으로 돌 수 있음
            if not board[old_y][old_x - 1] and not board[old_y + 1][old_x - 1]:
                new_x, new_y, new_type = old_x - 1, old_y - 1, 0
                if time_map[old_x][old_y][new_type] + 1 < time_map[new_x][new_y][new_type]:
                    time_map[new_x][new_y][new_type] = time_map[old_x][old_y][new_type] + 1
                    q.append((new_x, new_y, new_type))


def bfs():
    time_map[0][0] = [0, 0]
    while q:

        x, y, type_num = q.popleft()
        print("시작", x, y, type_num)
        # 상 하 좌 우
        move(x, y, type_num)
        # 축1, 축2 * 시계, 반시계
        rotate(x, y, type_num)

        for i in range(5):
            print(time_map[i])
        print(q)


time_map = [[[99999, 99999] for _ in range(N)] for __ in range(N)]  # [가로, 세로]
q = deque()
q.append((0, 0, 0))
bfs()  # type 0(가로), type 1(세로)
print(time_map[N - 1][N - 1])
