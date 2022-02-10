import sys

# 4831. 전기버스
sys.stdin = open('input.txt')

testcase = int(input())
for tc in range(testcase):
    # K: 한 번 충전으로 이동할 수 있는 정류장 수, N: 정류장 수
    # M: 충전기가 설치된 정류장의 수
    K, N, M = map(int, input().split())
    chargers = [False for _ in range(N)]
    charger_lst = list(map(int, input().split()))
    # 충전기 설치된 정류장 True 처리
    for charger in charger_lst:
        chargers[charger] = True
    cnt = 0
    now_station = 0

    # 충전기 찾는 코드
    # 5칸 전진후 뒤로가면서 찾음
    while now_station + K < N: # 종점 넘어가면 바로 탈출
        checker = 0
        for i in range(now_station + K, now_station, -1):
            if chargers[i]:
                checker = 1
                now_station = i
                cnt += 1
                break

        # 다시 5칸 백했는데도 없으면? --> 더 이상 못감
        if checker == 0:
            break

    # cheker == 1
    if checker:
        print(f'#{tc + 1} {cnt}')
    # cheker == 0
    else:
        print(f'#{tc + 1} {0}')
