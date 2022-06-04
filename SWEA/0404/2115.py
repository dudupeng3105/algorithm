# 꿀이익 함수 만들고
def calculate_revenue(honey_arr):
    result = 0
    honey_arr.sort(reverse=True)
    #print(honey_arr)
    for i in range(m):
        temp = 0
        temp_c = 0
        this = i
        while this < m:
            if temp_c + honey_arr[this] <= c_max:
                temp_c += honey_arr[this]
                temp += honey_arr[this] ** 2
                this += 1
            else:
                this += 1
        # 비교
        result = max(result, temp)

    return result


test_case = int(input())
for tc in range(1, test_case + 1):
    n, m, c_max = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 탐색 로직 만들고
    ans = 0
    for r in range(n):
        for c in range(n - m + 1):
            #print('#####################')
            temp_1 = calculate_revenue(arr[r][c:c + m])
            for i in range(n - r):
                if i == 0:  # 1번 꿀통과 같은 라인
                    for j in range(c + m, n - m + 1):
                        temp_2 = calculate_revenue(arr[r + i][j:j+m])
                        # 계산
                        temp_ans = temp_1 + temp_2
                        ans = max(temp_ans, ans)
                else:
                    for j in range(n - m + 1):
                        temp_2 = calculate_revenue(arr[r + i][j:j+m])
                        # 계산
                        temp_ans = temp_1 + temp_2
                        ans = max(temp_ans, ans)

    print(f'#{tc} {ans}')
