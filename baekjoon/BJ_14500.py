def angle_90(arr):  # 90도 회전
    row = len(arr)
    col = len(arr[0])
    new_arr = [[0 for _ in range(row)] for __ in range(col)]
    for i in range(row):
        for j in range(col):
            new_arr[j][row - 1 - i] = arr[i][j]

    return new_arr


def reverse_arr(arr):  # 좌우반전
    row = len(arr)
    col = len(arr[0])
    new_arr = [[0 for _ in range(col)] for __ in range(row)]
    for i in range(row):
        for j in range(col):
            new_arr[i][col - 1 - j] = arr[i][j]

    return new_arr


# 0. 맵 입력받기
N, M = map(int, input().split(' '))
#M, N = 6, 5
given_arr = [[0 for _ in range(M)] for __ in range(N)]

for i in range(N):
    given_arr[i] = list(map(int, input().split(' ')))
#given_arr = [[1, 2, 3, 4, 5, 6], [5, 4, 3, 2, 1, 2],  [3, 4, 1, 2, 8, 2],  [5, 1, 1, 1, 1, 10],  [5, 25, 3, 4, 9, 6]]
#print(given_arr)
# 1. 일자막대기 ==== ## N : 행 수 / M : 열의 수
# 맵 원상태
max_value = 0
sum = 0
for i in range(N):
    for j in range(M-3):
        sum = given_arr[i][j] + given_arr[i][j+1] + given_arr[i][j+2] + given_arr[i][j+3]
        max_value = max(max_value, sum)
# 맵 90도 회전 = 막대기 회전 이랑 같은 상황
given_arr_90 = angle_90(given_arr)
for i in range(M):
    for j in range(N-3):
        sum = given_arr_90[i][j] + given_arr_90[i][j+1] + given_arr_90[i][j+2] + given_arr_90[i][j+3]
        max_value = max(max_value, sum)

# 2. 정사각형 2*2 -> 맵 원상태만 하면 됨
for i in range(N-1):
    for j in range(M-1):
        sum = given_arr[i][j] + given_arr[i][j+1] + given_arr[i+1][j] + given_arr[i+1][j+1]
        max_value = max(max_value, sum)

# 3. -↑- 모양 -> 회전 4 세트
# 맵 원상태
for i in range(N-1):
    for j in range(M-2):
        sum = given_arr[i][j] + given_arr[i][j+1] + given_arr[i][j+2] + given_arr[i+1][j+1]
        max_value = max(max_value, sum)
# 90도 회전
for i in range(M-1):
    for j in range(N-2):
        sum = given_arr_90[i][j] + given_arr_90[i][j+1] + given_arr_90[i][j+2] + given_arr_90[i+1][j+1]
        max_value = max(max_value, sum)
# 180도 회전
given_arr_180 = angle_90(given_arr_90)
for i in range(N-1):
    for j in range(M-2):
        sum = given_arr_180[i][j] + given_arr_180[i][j+1] + given_arr_180[i][j+2] + given_arr_180[i+1][j+1]
        max_value = max(max_value, sum)
# 270도 회전
given_arr_270 = angle_90(given_arr_180)
for i in range(M-1):
    for j in range(N-2):
        sum = given_arr_270[i][j] + given_arr_270[i][j+1] + given_arr_270[i][j+2] + given_arr_270[i+1][j+1]
        max_value = max(max_value, sum)

#4. S 모양 --> 기존, 좌우, 90도, 90도 좌우
## N : 행 수 / M : 열의 수
# 맵 원상태
for i in range(N-2):
    for j in range(M-1):
        sum = given_arr[i][j] + given_arr[i+1][j] + given_arr[i+1][j+1] + given_arr[i+2][j+1]
        max_value = max(max_value, sum)
# 맵 좌우대칭
given_arr_rev = reverse_arr(given_arr)
for i in range(N-2):
    for j in range(M-1):
        sum = given_arr_rev[i][j] + given_arr_rev[i+1][j] + given_arr_rev[i+1][j+1] + given_arr_rev[i+2][j+1]
        max_value = max(max_value, sum)
# 맵 90도
for i in range(M-2):
    for j in range(N-1):
        sum = given_arr_90[i][j] + given_arr_90[i+1][j] + given_arr_90[i+1][j+1] + given_arr_90[i+2][j+1]
        max_value = max(max_value, sum)
# 맵 90도 좌우
given_arr_90_rev = reverse_arr(given_arr_90)
for i in range(M-2):
    for j in range(N-1):
        sum = given_arr_90_rev[i][j] + given_arr_90_rev[i+1][j] + given_arr_90_rev[i+1][j+1] + given_arr_90_rev[i+2][j+1]
        max_value = max(max_value, sum)
# 5. ㄱ자 모양 --> 8가지 있음 회전(4가지) 회전_좌우(4가지)
# 맵 원상태
for i in range(N-2):
    for j in range(M-1):
        sum = given_arr[i][j] + given_arr[i+1][j] + given_arr[i+2][j] + given_arr[i+2][j+1]
        max_value = max(max_value, sum)
# 90도 회전
for i in range(M-2):
    for j in range(N-1):
        sum = given_arr_90[i][j] + given_arr_90[i+1][j] + given_arr_90[i+2][j] + given_arr_90[i+2][j+1]
        max_value = max(max_value, sum)
# 180도 회전
for i in range(N-2):
    for j in range(M-1):
        sum = given_arr_180[i][j] + given_arr_180[i+1][j] + given_arr_180[i+2][j] + given_arr_180[i+2][j+1]
        max_value = max(max_value, sum)
# 270도 회전
for i in range(M-2):
    for j in range(N-1):
        sum = given_arr_270[i][j] + given_arr_270[i+1][j] + given_arr_270[i+2][j] + given_arr_270[i+2][j+1]
        max_value = max(max_value, sum)

# 맵 원상태
for i in range(N-2):
    for j in range(M-1):
        sum = given_arr_rev[i][j] + given_arr_rev[i+1][j] + given_arr_rev[i+2][j] + given_arr_rev[i+2][j+1]
        max_value = max(max_value, sum)
# 90도 회전 좌우
for i in range(M-2):
    for j in range(N-1):
        sum = given_arr_90_rev[i][j] + given_arr_90_rev[i+1][j] + given_arr_90_rev[i+2][j] + given_arr_90_rev[i+2][j+1]
        max_value = max(max_value, sum)
# 180도 회전 좌우
given_arr_180_rev = reverse_arr(given_arr_180)
for i in range(N-2):
    for j in range(M-1):
        sum = given_arr_180_rev[i][j] + given_arr_180_rev[i+1][j] + given_arr_180_rev[i+2][j] + given_arr_180_rev[i+2][j+1]
        max_value = max(max_value, sum)
# 270도 회전
given_arr_270_rev = reverse_arr(given_arr_270)
for i in range(M-2):
    for j in range(N-1):
        sum = given_arr_270_rev[i][j] + given_arr_270_rev[i+1][j] + given_arr_270_rev[i+2][j] + given_arr_270_rev[i+2][j+1]
        max_value = max(max_value, sum)

print(max_value)
# 성공 --> 백준 메모리 47892kb, 시간 2912ms