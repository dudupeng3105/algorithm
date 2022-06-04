# 각 자리수 합 3의 배수여야함
a = list(map(int, input()))

if 0 not in a:
    print(-1)
else:
    if sum(a) % 3:  # 3의 배수 아님
        print(-1)
    else:  # 3의 배수
        a.sort(reverse=True)
        ans = ''
        for num in a:
            ans = ans + str(num)
        print(ans)