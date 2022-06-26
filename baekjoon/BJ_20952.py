import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
a_7 = a[::]
b = list(map(int, input().split()))
b_7 = [0 for _ in range(m)]
op_check = [False for _ in range(m)]

# % 7 처리 미리 한 번 하기
for i in range(m):
    b_7[i] = b[i] % 7

# m 번의 연산
# 단, 연산을 수행한 결과 수열 A의 모든 원소가 제거된다면 해당 연산은 수행하지 않는다.
not_0_cnt = n
for i in range(m):
    # 연산 전 모두 제거되는지 체크
    temp_cnt = not_0_cnt
    for j in range(n):
        if a_7[j] == 0:
            continue
        else:
            if (a_7[j] + b_7[i]) % 7 == 0:
                temp_cnt -= 1

    if temp_cnt:  # 남아있는게 있으면
        op_check[i] = True
        # 진짜 연산
        for j in range(n):
            if a_7[j] == 0:
                continue
            else:
                a_7[j] = (a_7[j] + b_7[i]) % 7
                if a_7[j] == 0:
                    not_0_cnt -= 1

cnt = 0
result = []
for i in range(n):
    if a_7[i]:
        cnt += 1
        for j in range(m):
            if op_check[j]:
                a[i] = (a[i] + b[j]) % (10 ** 9 + 7)
        result.append(a[i])

print(cnt)
print(*result)
