import sys

n = int(sys.stdin.readline())
dice_dict = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}  # 주사위의 위치관계 정의
arr = [[] for _ in range(n)]
junction = []
for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().split()))

result = 0
for i in range(6):
    bottom = arr[0]
    junction = [bottom[i], bottom[dice_dict[i]]]

    for j in range(1, n):
        next_dice = arr[j]
        for k in range(6):
            if junction[j] == next_dice[k]:
                junction.append(next_dice[dice_dict[k]])

    # 최대값 구하기
    temp = 0
    for t in range(n):
        bot, top = junction[t], junction[t+1]
        for a in range(6, 0, -1):
            if a != top and a != bot:
                temp += a
                break

    if temp > result:
        result = temp

print(result)