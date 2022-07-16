import sys

input = sys.stdin.readline


arr = [False for _ in range(10000)]
check = [False for _ in range(10000)]
for i in range(1111, 10000):
    temp = list(map(int, str(i)))
    if 0 in temp:
        continue
    else:
        if check[i]:
            continue

        clock_num = i
        check[i] = True
        # 1
        num = 1000*temp[1] + 100 * temp[2] + 10 * temp[3] + temp[0]
        check[num] = True
        if num < clock_num:
            clock_num = num
        # 2
        num = 1000 * temp[2] + 100 * temp[3] + 10 * temp[0] + temp[1]
        check[num] = True
        if num < clock_num:
            clock_num = num
        # 3
        num = 1000 * temp[3] + 100 * temp[0] + 10 * temp[1] + temp[2]
        check[num] = True
        if num < clock_num:
            clock_num = num

        # print(clock_num)
        arr[clock_num] = True

n = list(map(int, input().split()))
temp = []
temp.append(1000*n[0] + 100 * n[1] + 10 * n[2] + n[3])
temp.append(1000*n[1] + 100 * n[2] + 10 * n[3] + n[0])
temp.append(1000*n[2] + 100 * n[3] + 10 * n[0] + n[1])
temp.append(1000*n[3] + 100 * n[0] + 10 * n[1] + n[2])
min_temp = min(temp)
cnt = 0
for i in range(1111, min_temp+1):
    if arr[i]:
        cnt += 1

print(cnt)

# for i in range(10000):
#     if arr[i]:
#         print(i)









