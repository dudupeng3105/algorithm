import sys
# 나무꾼 이다솜
input = sys.stdin.readline

n, c, w = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

last = max(arr)
ans = 0
for l in range(1, last + 1):
    piece_cnt = 0
    cut = 0
    for tree in arr:
        piece = tree // l
        if tree % l == 0:  # 나누어 떨어짐
            if piece * w * l - (piece-1) * c > 0: # 16 -> 4 / 4 / 4 /4 -> cut 3, piece 4
                piece_cnt += piece
                cut += piece - 1
        else:
            if piece * w * l - piece * c > 0:  # 15 4 / 4 / 4 / 3 -> cut 3, piece 3
                piece_cnt += piece
                cut += piece

    temp = piece_cnt * w * l - cut * c
    if temp > ans:
        ans = temp

print(ans)
