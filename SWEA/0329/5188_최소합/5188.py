test_case = int(input())

for tc in range(1, test_case + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    len_path = 2 * (n-1)
    ans = 99999999
    for b in range((1 << (n - 1)) - 1, 1 << 2 * (n - 1)):  # 0011 ~ 1111 (n=3)
        combi_lst = []
        flag = 1
        cnt_one = 0
        cnt_zero = 0
        for i in range(len_path):
            if b & (1 << i):  # 그자리가 1이면(오른쪽)
                cnt_one += 1
                combi_lst.append(1)
                if cnt_one >= n:
                    flag = 0
                    break
            else:  # 그자리가 0 이면(아래로)
                cnt_zero += 1
                combi_lst.append(0)
                if cnt_zero >= n:
                    flag = 0
                    break

        # 계산 및 대소 비교
        if flag:
            temp = arr[0][0]
            r, c = 0, 0
            print(combi_lst)
            for bin_num in combi_lst:
                if bin_num:  # 1
                    r, c = r, c + 1
                    temp += arr[r][c]
                else:  # 0
                    r, c = r + 1, c
                    temp += arr[r][c]

            if temp < ans:
                ans = temp

    print(f'#{tc} {ans}')
