c, r = map(int, input().split())
find_num = int(input())
arr = [[0 for _ in range(c)] for __ in range(r)]
num = 1  # 1~n*n 채워넣기
i = r-1
j = 0
path_checker = 2  # x 축 양의 방향 전진
if find_num > c*r:
    print(0)
else:
    if find_num == 1:
        print(1, 1)
    else:
        while num < c*r + 1:
            arr[i][j] = num
            if path_checker == 1:  # x 축 양의 방향 전진
                if j == c - 1 or arr[i][j + 1]:
                    path_checker = 4  # y 축 음의 방향으로 전환
                    i += 1
                else:
                    j += 1

            elif path_checker == 4:  # y 축 음의 방향으로 전환
                if i == r - 1 or arr[i + 1][j]:
                    path_checker = 3  # x 축 음의 방향 전진
                    j -= 1
                else:
                    i += 1

            elif path_checker == 3:  # x 축 음의 방향 전진
                if j == 0 or arr[i][j - 1]:
                    path_checker = 2  # y 축 양의 방향 전진
                    i -= 1
                else:
                    j -= 1

            elif path_checker == 2:  # y 축 양의 방향 전진
                if i == 0 or arr[i - 1][j]:
                    path_checker = 1  # x 축 양의 방향 전진
                    j += 1
                else:
                    i -= 1

            num += 1
            if num == find_num:
                print(j+1, r-i)
