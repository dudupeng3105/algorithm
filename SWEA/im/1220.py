import sys
sys.stdin = open("test.txt")

for tc in range(1, 11):
    n = int(input())
    arr = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        arr[i] = list(map(int, input().split()))

    # 세로로 체크하면서
    result = 0
    for c in range(n):
        prev_magnetic = 0
        for r in range(n):
            magnetic = arr[r][c]
            if magnetic == 0:
                continue
            elif magnetic == 1:  # N극
                prev_magnetic = magnetic
            else:  # s극 magnetic 2
                if prev_magnetic == 1:
                    result += 1 # n극 다음에 s극 와야 교착
                    prev_magnetic = 0

    print(f'#{tc} {result}')
