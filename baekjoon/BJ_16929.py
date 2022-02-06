import sys
sys.setrecursionlimit(10**6)

def dfs(r, c, depth, color):
    
    for i in range(4):
        new_r, new_c = r + dx[i], c + dy[i]
        # 맵 밖으로 나가거면 돌아옴
        if new_r < 0 or new_r > row-1 or new_c <0 or new_c > col-1:
            continue
        # 4개이상이고 시작 row, col과 같으면 종료
        if depth >=4 and new_r == start_row and new_c == start_col:
            print('Yes')
            exit(0)

        # 이미 방문했거나 색깔이 다르면 더 안가고 돌아옴
        if visited[new_r][new_c] == False and \
            arr[new_r][new_c] == color:
            visited[new_r][new_c] = True
            dfs(new_r, new_c, depth+1, color)
            visited[new_r][new_c] = False
    
    return   


# 입력 받기
row, col = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(col)] for __ in range(row)]
for r in range(row):
    arr[r] = list(map(str, sys.stdin.readline().rstrip()))

#dfs 돌리기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False for _ in range(col)] for __ in range(row)]
for r in range(row):
    for c in range(col):
        if visited[r][c] == False:            
            visited[r][c] = True
            start_row = r
            start_col = c
            color = arr[r][c]            
            dfs(r, c, 1, color)

print('No')