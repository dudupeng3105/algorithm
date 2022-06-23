import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

# 역순으로 간다이
cnt = 0
next_want_num = arr[-1]
for i in range(n-1, -1, -1):
    this_num = arr[i]  # 확인할 수
    if this_num < next_want_num:  # 작으면 조건 만족하니까
        # cnt += 0
        next_want_num = this_num - 1  # 그 다음 수는 최소 이 수보다 1이 작아야함 => next_want_num
    else:  # 최소 조건을 만족하는 수보다 커버리면 어쩔수없이 바꿔줘야함
        cnt += this_num - next_want_num  # 1씩 바뀌니까 최소 조건을 만족하는 수까지 바꿔줌
        next_want_num = next_want_num - 1  # 그 다음 수는 최소 이 수보다 1이 작아야함

print(cnt)


