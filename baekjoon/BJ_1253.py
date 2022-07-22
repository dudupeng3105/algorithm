import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 투 포인터
def two_pointer(index, target):
    s, e = 0, len(arr) - 1

    if s == index:  # 자기 자신 안들어가게
        s += 1
    if e == index:  # 자기 자신 안들어가게
        e -= 1

    while s < e:
        summ = arr[s] + arr[e]

        if target == summ:
            return 1
        elif target > summ:
            s += 1
            if s == index:  # 자기 자신 안들어가게
                s += 1
        else:
            e -= 1
            if e == index:  # 자기 자신 안들어가게
                e -= 1

    return 0


arr.sort()

cnt = 0
for i in range(n):
    cnt += two_pointer(i, arr[i])

print(cnt)
