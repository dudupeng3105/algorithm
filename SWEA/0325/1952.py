test_case = int(input())
# dp로 품
for tc in range(1, test_case + 1):
    price_lst = list(map(int, input().split()))  # 일, 월, 3달, 1년
    days = [0] + list(map(int, input().split()))
    dp = [0 for _ in range(13)]

    for i in range(1, 13):
        if i >= 3:  # 3월 이상
            temp = dp[i - 1] + min(price_lst[0] * days[i], price_lst[1])
            dp[i] = min(temp, dp[i-3] + price_lst[2])
        else:
            dp[i] = dp[i-1] + min(price_lst[0]*days[i], price_lst[1])

    # 마지막 비교
    dp[12] = min(dp[12], price_lst[3])
    print(f'#{tc} {dp[12]}')