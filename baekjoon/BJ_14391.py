N, M = map(int, input().split())
arr = [[0 for _ in range(M)] for __ in range(N)]
for i in range(N):
    arr[i] = list(map(str, input()))

# 가로로 자르기
result = 0
temp = 0
for i in range(N):
    num_str = ''
    for e in arr[i]:
        num_str += e
    temp += int(num_str)

result = max(temp, result)

# 세로로 자르기
temp = 0
for i in range(M):
    num_str = ''
    for j in range(N):
        num_str += arr[j][i]
    temp += int(num_str)

result = max(temp, result)

print(result)