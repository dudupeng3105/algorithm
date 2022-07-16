import sys
from itertools import product

input = sys.stdin.readline


def rotate_90():
    global lst
    lst = list(map(list, zip(*lst[::-1])))


def rotate_reverse():
    global lst
    lst = list(map(list, zip(*lst)))[::-1]

def left():
    global lst
    for i in range(n):
        if 0 in lst[i]:
            cnt = 0
            while 0 in lst[i]:
                lst[i].remove(0)
                cnt += 1
            for u in range(cnt):
                lst[i].append(0)
        chk = [False for _ in range(n)]
        for j in range(0, n-1):
            k = j + 1
            if lst[i][j] == lst[i][k] and chk[j] is False and chk[k] is False:
                lst[i][j] += lst[i][k]
                lst[i][k] = 0
                chk[j] = True
                chk[k] = True
        if 0 in lst[i]:
            cnt = 0
            while 0 in lst[i]:
                lst[i].remove(0)
                cnt += 1
            for u in range(cnt):
                lst[i].append(0)

    return


def right():
    rotate_90()
    rotate_90()
    left()
    rotate_reverse()
    rotate_reverse()
    return


def up():
    rotate_90()
    rotate_90()
    rotate_90()
    left()
    rotate_reverse()
    rotate_reverse()
    rotate_reverse()
    return


def down():
    rotate_90()
    left()
    rotate_reverse()
    return


# main
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
#print(arr)
ans = 0
op = [0, 1, 2, 3]
ops = list(product(op, repeat=5))  # 길이 5 오퍼레이션 조합

# 로직
copys = [item[:] for item in arr]
for op in ops:
    lst = [item[:] for item in arr]
    for arrow in op:
        if arrow == 0:
            left()
        elif arrow == 1:
            up()
        elif arrow == 2:
            down()
        elif arrow == 3:
            right()

    temp_max = 0
    for i in range(n):
        for j in range(n):
            if lst[i][j] > temp_max:
                temp_max = lst[i][j]

    ans = max(temp_max, ans)

print(ans)
