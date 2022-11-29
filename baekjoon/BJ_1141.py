import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(input().rstrip())

arr.sort()
cnt = 1
pre = arr[0]
for i in range(1, n):
    next_word = arr[i]
    # 길이 미만
    if len(next_word) < len(pre):
        cnt += 1
    else:
        if pre != next_word[:len(pre)]:
            cnt += 1
        else:
            cnt += 0

    pre = next_word

print(cnt)
