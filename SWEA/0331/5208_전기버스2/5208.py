test_case = int(input())

for tc in range(1, test_case + 1):
    given_lst = list(map(int, input().split()))
    last_station = given_lst[0]
    battery_lst = [0] + given_lst[1:]
    dp = [1000 for _ in range(last_station + 1)]
    dp[1] = -1  # 첫 정류장 -1 처리(계산 용이)
    for station in range(1, last_station):
        for next_station in range(station + 1, station + battery_lst[station] + 1):
            if next_station > last_station:
                break
            else:
                if dp[next_station] > dp[station] + 1:
                    dp[next_station] = dp[station] + 1

    print(dp)
    print(f'#{tc} {dp[last_station]}')
