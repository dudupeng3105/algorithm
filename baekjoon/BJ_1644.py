n = int(input())

# 에라토스테네스의 체
a = [False, False] + [True] * (n-1)
primes = []

for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

# print(primes)
# 투 포인터
left_point = 0
right_point = 0
cnt = 0
if n == 1:
    print(0)
else:
    temp_sum = primes[0]
    while left_point <= right_point:
        # print(left_point, right_point)
        if temp_sum == n:
            cnt += 1
            right_point += 1
            if right_point > len(primes) - 1:
                break
            temp_sum += primes[right_point]
        elif temp_sum > n:
            temp_sum -= primes[left_point]
            left_point += 1
        else:  # temp_sum < n
            right_point += 1
            if right_point > len(primes)-1:
                break
            temp_sum += primes[right_point]

    print(cnt)



