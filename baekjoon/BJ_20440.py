# 20440 모기문제
import sys

input = sys.stdin.readline

n = int(input())
inout = []

for i in range(n):
    s, e = map(int, input().split())
    inout.append((s, 1))
    inout.append((e, -1))

inout.sort()
inout.append((-1, -1))  # 밑에 로직의 편안함을 위해

idx = 0
start = -1
end = -1
max_cnt = 0
temp_cnt = 0
cnt = 0
flag = 0
while idx < 2 * n:

    temp_cnt = inout[idx][1]
    while inout[idx][0] == inout[idx + 1][0]:  # 같은 시간들
        idx += 1
        temp_cnt += inout[idx][1]
    #print(cnt, temp_cnt)
    # cnt 업데이트
    if temp_cnt > 0:  # 모기수가 늘어남
        cnt += temp_cnt
        if cnt > max_cnt:
            max_cnt = cnt
            start = inout[idx][0]
            flag = 1

    elif temp_cnt == 0:
        idx += 1
        continue

    else:  # 모기수가 줄어듬
        #print("들어옴", cnt, temp_cnt)
        if cnt == max_cnt and flag:  # 현재 cnt가 max_cnt였다면 이게 끝난거임
            end = inout[idx][0]
        cnt += temp_cnt
        flag = 0

    idx += 1

print(max_cnt)
print(start, end)
