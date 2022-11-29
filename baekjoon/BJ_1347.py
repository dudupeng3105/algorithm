import sys
# 미로만들기
input = sys.stdin.readline

n = int(input())
# 0 북쪽 1 동쪽 2 남쪽 3 서쪽
x, y = 0, 0

moves = input().rstrip()
view_dir = 2  # 남쪽
dxy = [(0, -1), (1, 0), (0, 1), (-1, 0)]
arr = [(0, 0)]
for i in range(n):
    move = moves[i]
    if move == 'R':
        view_dir = (view_dir + 1) % 4
    elif move == 'L':
        view_dir = (view_dir - 1) % 4
    else:  # move F
        dx, dy = dxy[view_dir]
        x, y = x + dx, y + dy
        arr.append((x, y))

arr.sort()
start_x = arr[0][0]
end_x = arr[-1][0]

arr.sort(key=lambda i: i[1])
start_y = arr[0][1]
end_y = arr[-1][1]

for r in range(start_y, end_y + 1):
    s = ''
    for c in range(start_x, end_x + 1):
        if (c, r) in arr:
            s += '.'
        else:
            s += '#'
    print(s)
