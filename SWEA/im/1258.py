import sys

sys.stdin = open("test.txt")

test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input())
    arr = [[0 for _ in range(n)] for __ in range(n)]
    truth_map = [[False for _ in range(n)] for __ in range(n)]
    for i in range(n):
        arr[i] = list(map(int, input().split()))

    result_lst = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0 and truth_map[i][j] == False:
                w, h = 1, 1 # 초기화
                # 가로방향
                for c in range(j+1, n):
                    if arr[i][c] == 0:
                        break
                    else:
                        w += 1
                # 세로방향
                for r in range(i+1, n):
                    if arr[r][j] == 0:
                        break
                    else:
                        h += 1
                # 결과 저장
                result_lst.append([h, w])  #[행, 열]
                # 방문체크
                for y in range(i, i+h):
                    for x in range(j, j+w):
                        truth_map[y][x] = True
            else:
                truth_map[i][j] = True
    result_lst.sort(key=lambda x: (x[0]*x[1], x[0]))  # 1순위 키 넓이, 2순위 키 행
    # 출력
    print(f'#{tc} {len(result_lst)}', end=" ")
    for h, w in result_lst:
        print(h, w, end=" ")
    print()