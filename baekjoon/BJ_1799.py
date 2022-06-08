import sys
input = sys.stdin.readline


def dfs(num, depth):
    global ans_chess_num, color
    ans_chess_num = max(ans_chess_num, depth)
    if num >= n*n:
        return

    r, c = num // n, num % n
    if n % 2 == 0:  # n이 짝수이고
        if r % 2 == 1:
            if color:  # 1
                c += 1
            else:
                c -= 1

    if chess_map[r][c] == 1:
        if diagonal_upward[r+c] == False and diagonal_downward[r + (n-1) - c] == False:
            # 1번 둔다
            diagonal_upward[r + c] = True
            diagonal_downward[r + (n-1) - c] = True
            dfs(num + 2, depth + 1)  # row, col, depth(체스의 수)
            diagonal_upward[r + c] = False
            diagonal_downward[r + (n-1) - c] = False
            # 2번 안두고 넘어간다.
            dfs(num + 2, depth)  # 다음 자리 알아봄
        else:
            dfs(num + 2, depth)  # 다음 자리 알아봄

    else:  # 둘 수 없는 자리
        dfs(num + 2, depth)  # 다음 자리 알아봄


n = int(input())
chess_map = [list(map(int, input().split())) for _ in range(n)]
# 1은 놓을 수 있는 곳
diagonal_upward = [False for _ in range(2*n - 1)]
diagonal_downward = [False for _ in range(2*n - 1)]

ans_chess_num = 0
result = 0
color = 1 # black
for i in range(0, n*n, 2):
    r, c = i // n, i % n
    if n % 2 == 0:  # n이 짝수이고
        if r % 2 == 1:
            if color:  # 1
                c += 1
            else:
                c -= 1
    if chess_map[r][c] == 1:
        diagonal_upward[r+c] = True
        diagonal_downward[r+(n-1)-c] = True
        dfs(i + 2, 1)  # row, col, depth(체스의 수)
        diagonal_upward[r + c] = False
        diagonal_downward[r + (n-1) - c] = False
        dfs(i + 2, 0)
        break


result += ans_chess_num
ans_chess_num = 0
color = 0  # white
for i in range(1, n*n, 2):
    r, c = i // n, i % n
    if n % 2 == 0:  # n이 짝수이고
        if r % 2 == 1:
            if color:  # 1
                c += 1
            else:
                c -= 1
    if chess_map[r][c] == 1:
        diagonal_upward[r+c] = True
        diagonal_downward[r+(n-1)-c] = True
        dfs(i + 2, 1)  # row, col, depth(체스의 수)
        diagonal_upward[r + c] = False
        diagonal_downward[r + (n-1) - c] = False
        dfs(i + 2, 0)
        break

result += ans_chess_num
print(result)