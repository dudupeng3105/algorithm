import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
d = [[-1, 0], [0, -1], [1, 0], [0, 1]]
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            R = [i, j]
            board[i][j] = '.'
        elif board[i][j] == 'B':
            B = [i, j]
            board[i][j] = '.'
        elif board[i][j] == 'O':
            O = [i, j]
            board[i][j] = '.'

q = deque()
loc = R + B
q.append(loc)  # 앞 두 개[0,1]는 red 뒤 두 개[2,3]는 blue 좌표다.
cnt = 0
visited = defaultdict(int)
visited[f'{loc}']
while q and cnt < 10:
    cnt += 1
    for _ in range(len(q)):
        loc = q.popleft()
        ry, rx, by, bx = loc

        for dy, dx in d:
            # 일단 빨간거 부터 굴려보자
            tRy, trx = ry, rx
            rclear, bclear = False, False

            while board[tRy + dy][trx + dx] != '#':  # 벽 만나기 전까지 구른다.
                tRy, trx = tRy + dy, trx + dx

                if tRy == O[0] and trx == O[1]:  # 골인 시 rclear를 해주고 break
                    rclear = True
                    break

            tby, tbx = by, bx
            while board[tby + dy][tbx + dx] != '#':  # 벽 만나기 전까지 구른다.
                tby, tbx = tby + dy, tbx + dx

                if tby == O[0] and tbx == O[1]:  # 골인 시 rclear를 해주고 break
                    bclear = True
                    break

            # 두 구슬이 같은 위치에 있을 수는 없다.
            if tRy == tby and trx == tbx:  # 한 구슬이 한 구슬 뒤에 위치해야 한다.
                if [dy, dx] == [-1, 0]:  # 위로 굴린 경우
                    if ry < by:  # 빨간 구슬이 더 위에 있던 경우 파란 구슬 뒤로 물려줌
                        tby += 1
                    else:
                        tRy += 1
                elif [dy, dx] == [0, -1]:  # 좌로 굴린 경우
                    if rx < bx:  # 빨간 구슬이 더 좌에 있던 경우 파란 구슬 뒤로 물려줌
                        tbx += 1
                    else:
                        trx += 1
                elif [dy, dx] == [1, 0]:  # 아래로 굴린 경우
                    if ry < by:  # 빨간 구슬이 더 좌에 있던 경우 파란 구슬 뒤로 물려줌
                        tRy -= 1
                    else:
                        tby -= 1
                elif [dy, dx] == [0, 1]:  # 우로 굴린 경우
                    if rx < bx:  # 빨간 구슬이 더 좌에 있던 경우 파란 구슬 뒤로 물려줌
                        trx -= 1
                    else:
                        tbx -= 1

            if rclear and not bclear:
                print(1)
                sys.exit(0)

            if not bclear:
                new = [tRy, trx, tby, tbx]
                if visited[f'{new}'] == 0:
                    q.append(new)
                    visited[f'{new}'] = 1

print(0)