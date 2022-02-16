import sys
sys.stdin = open('input.txt')
import random

# 좌,우 이동 가능한 곳을 먼저 탐색하고
# 아래 이동 가능 탐색 순으로 설정
dx = [0, 0, 1]
dy = [-1, 1, 0]

def ladder_search(x, y):
    # 전체 사다리 크기와 동일한 방문 표시용 2차원 리스트
    visited = [[0]*10 for _ in range(10)]
    # 처음 시작지점 방문 표시
    visited[x][y] = 1
    # 행 index가 9가 되기 전까지 반복
    while x != 9:
        # 좌, 우, 하 순으로 조회
        for i in range(3):
            # 다음 조회지역 index 설정
            nx = x + dx[i]
            ny = y + dy[i]

            #다음 조회 지역이 범위를 벗어나지 않고 / 아직 방문하기 전이라면
            if 0 <= nx < 10 and 0 <= ny < 10 and visited[nx][ny] == 0:
                # 다음 방문지역이 1이라면 이동
                if arr[nx][ny] == 1:
                    # 이미 왔던 길을 돌아가지 않기 위해
                    # 방문 표시
                    visited[nx][ny] = 1
                    # 내 현재 위치 변경
                    x, y = nx, ny
                # 다음 방문지역이 2라면
                elif arr[nx][ny] == 2:
                    # 도착지점의 y index 반환후 종료
                    return ny

arr = [list(map(int, input().split())) for _ in range(10)]
for j in range(10):
    # (0, i)가 1 == 시작지점
    # 모든 시작지점에서
    if arr[0][j] == 1:
        # 도착지점을 찾기위한 탐색 시작
        result = ladder_search(0, j)

print(f'#{result}')