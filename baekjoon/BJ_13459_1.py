from collections import deque

# Get Param.
N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

# Set Init Param.
q = deque()
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


# Set Func.
def init():
    redX, redY, blueX, blueY = [0] * 4

    for row in range(N):
        for col in range(M):
            if board[row][col] == 'R':
                redX, redY = row, col

            elif board[row][col] == 'B':
                blueX, blueY = row, col

            # Init Spot
    q.append((redX, redY, blueX, blueY, 1))
    visited[redX][redY][blueX][blueY] = True


def move(x, y, dx, dy, count):
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count


def bfs():
    while q:
        rX, rY, bX, bY, depth = q.popleft()

        # if
        if depth > 10:
            break

        # 4 - Direction
        for i in range(4):
            nRx, nRy, rCnt = move(rX, rY, dx[i], dy[i], 0)
            nBx, nBy, bCnt = move(bX, bY, dx[i], dy[i], 0)

            # Check Escape
            if board[nBx][nBy] == 'O':
                continue
            if board[nRx][nRy] == 'O':
                print(1)
                return

            # Check Same Spot
            if nRx == nBx and nRy == nBy:
                if rCnt > bCnt:
                    nRx, nRy = nRx - dx[i], nRy - dy[i]
                else:
                    nBx, nBy = nBx - dx[i], nBy - dy[i]

            # Check Visited Arr
            if not visited[nRx][nRy][nBx][nBy]:
                visited[nRx][nRy][nBx][nBy] = True
                q.append((nRx, nRy, nBx, nBy, depth + 1))
    print(0)  # Any Escape not exist


## Start
init()
bfs()