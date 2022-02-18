import sys
from collections import deque


def bfs():
    q = deque()
    q.append((0, 0))  # pos, dice_num
    while q:
        pos, dice_num = q.popleft()
        # 종료조건
        if pos == 99:
            print(dice_num)
            return

        row = pos // 10
        col = pos % 10
        game_map[row][col] = True  # 방문 체크

        for i in range(1, 7):  # 주사위
            new_pos = pos + i

            if new_pos > 99:
                continue

            row = new_pos // 10
            col = new_pos % 10

            if game_map[row][col]:  # 이미왔으면
                continue

            if ladder[new_pos]:  # 사다리 있으면
                game_map[row][col] = True  # 사다리 출발점도 방문체크
                new_pos = ladder[new_pos]
                q.append((new_pos, dice_num + 1))
                continue

            if snake[new_pos]:  # 뱀 있으면
                game_map[row][col] = True  # 뱀 출발점도 방문체크
                new_pos = snake[new_pos]
                q.append((new_pos, dice_num + 1))
                continue

            q.append((new_pos, dice_num + 1))


game_map = [[False for _ in range(10)] for __ in range(10)]
ladder = [0 for _ in range(101)]
snake = [0 for _ in range(101)]

ladder_num, snake_num = map(int, sys.stdin.readline().split())
for _ in range(ladder_num):
    start, end = map(int, sys.stdin.readline().split())
    ladder[start-1] = end-1

for _ in range(snake_num):
    start, end = map(int, sys.stdin.readline().split())
    snake[start-1] = end-1

bfs()