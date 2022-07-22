import sys

input = sys.stdin.readline

arr = [False for _ in range(10000)]
check = [False for _ in range(10000)]
# 시계수를 모두 구함
for i in range(1111, 10000):
    temp = list(map(int, str(i)))
    if 0 in temp:
        continue
    else:
        if check[i]:  # check -> 시계수 검정을 한 수인가, 했으면 안해도됨
            continue

        clock_num = i
        check[i] = True
        # 1
        num = 1000 * temp[1] + 100 * temp[2] + 10 * temp[3] + temp[0]
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
        # 시계수를 담음
        arr[clock_num] = True

n = list(map(int, input().split()))
temp = []
temp.append(1000 * n[0] + 100 * n[1] + 10 * n[2] + n[3])
temp.append(1000 * n[1] + 100 * n[2] + 10 * n[3] + n[0])
temp.append(1000 * n[2] + 100 * n[3] + 10 * n[0] + n[1])
temp.append(1000 * n[3] + 100 * n[0] + 10 * n[1] + n[2])
# 입력받은 수의 시계수 구하고
min_temp = min(temp)
cnt = 0
# 어디에 있는 지 구함
for i in range(1111, min_temp + 1):
    if arr[i]:
        cnt += 1

print(cnt)