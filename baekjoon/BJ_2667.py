import sys


def dfs(row, col):
    # 땅이 아니면 return
    global town_size
    if row < 0 or row > N-1 or col <0 or col > N-1\
    or arr[row][col] == '0':
        return

    town_size += 1 
    arr[row][col] = '0' # 체크했으니 빈칸으로 만들어버림
    # 4방향 탐색
    dfs(row+1, col) # 오른쪽
    dfs(row, col+1) # 아래방향
    dfs(row-1, col) # 왼쪽
    dfs(row, col-1) # 위방향    

N = int(sys.stdin.readline())
arr = [[0 for _ in range(N)] for __ in range(N)]

for i in range(N):
    arr[i] = list(sys.stdin.readline().rstrip())

# arr 탐색
town_num = 0 # 단지 수
result_town_size = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            town_size = 0
            dfs(i, j)            
            result_town_size.append(town_size)
            town_num += 1

print(town_num)
result_town_size = sorted(result_town_size)
for ts in result_town_size:
    print(ts)