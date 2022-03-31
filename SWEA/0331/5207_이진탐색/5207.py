def binary_search(n, left, right):
    global cnt, flag

    while left <= right:
        m = (left + right) // 2
        middle_num = a_nums[m]

        if n == middle_num:
            flag = 0  # 성공
            return flag

        elif n < middle_num:
            cnt += 1
            if cnt == 2:
                flag = 1  # 실패
                return flag
            else:
                cnt = 1  # 좌라는 표시
            right = m - 1

        elif n > middle_num:
            cnt -= 1
            if cnt == -2:
                flag = 1  # 실패
                return flag
            else:  #
                cnt = -1  # 우라는 표시
            left = m + 1

    # 못찾을 때
    return flag


test_case = int(input())
for tc in range(1, test_case + 1):
    a, b = map(int, input().split())
    a_nums = list(map(int, input().split()))
    a_nums.sort()
    b_nums = list(map(int, input().split()))
    length_a = len(a_nums)
    ans = 0
    for b_num in b_nums:
        cnt, flag = 0, 1
        result = binary_search(b_num, 0, length_a - 1)
        if not flag:
            ans += 1

    print(f'#{tc} {ans}')
