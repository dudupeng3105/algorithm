import sys


def dfs(row):
    global cnt
    # n개의 체스 다 놓았으면
    if row == n - 1:
        cnt += 1
        return

    for i in range(n):
        next_r, next_c = row + 1, i

        flag = 0
        for check_row in range(row + 1):
            if queen_pos[check_row] == next_c:  #열이같으면
                flag = 1
                break
            if next_r-check_row == abs(queen_pos[check_row]-next_c):
                flag = 1
                break

        if flag:
            continue
        else:
            queen_pos[next_r] = i
            dfs(next_r)


n = int(sys.stdin.readline())
queen_pos = [-1 for _ in range(n)]
cnt = 0
for i in range(n):
    queen_pos[0] = i
    dfs(0)
print(cnt)
