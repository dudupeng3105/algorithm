import sys

sys.stdin = open("test.txt")

test_case = int(input())
for tc in range(1, test_case + 1):
    n, m = map(int, input().split())  # n=> n*n 행렬 m-> 회문의 길이
    arr = [[] for _ in range(n)]
    for i in range(n):
        arr[i] = list(input())

    # 가로 확인
    for i in range(n):
        for j in range(n - m + 1):  # 회문의 시작 인덱스
            if arr[i][j:j + m] == arr[i][j:j + m][::-1]:
                result = arr[i][j:j + m]
                break

    # 세로 확인
    flag = 0
    for j in range(n):
        for i in range(n - m + 1):  # 회문의 시작 인덱스
            temp = ''
            for k in range(i, i + m): # 시작인덱스부터 시작 + 회문의 길이
                temp += arr[k][j]  # 열은 고정, 행 하나씩 내려가며 temp에 추가

            # 만들어진 temp 회문 체크
            if temp == temp[::-1]:
                flag = 1
                result = temp
                break

        if flag:
            break

    print(f'#{tc}', end=' ')
    print(''.join(result))
