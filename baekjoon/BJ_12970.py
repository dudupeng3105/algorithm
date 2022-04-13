n, k = map(int, input().split())

a_num = 0
b_num = n

# 큰 범위 찾기
flag = 1
while flag and a_num < n + 1:
    temp_k = a_num * b_num
    if temp_k >= k:
        flag = 0
    else:
        a_num += 1
        b_num -= 1

if flag:  # 못찾았으면
    print(-1)

else:
    # print(a_num)
    # print(temp_k)

    ab_lst = ['A' for _ in range(a_num)] + ['B' for __ in range(b_num)]
    difference = temp_k - k
    main_pivot = a_num - 1
    pivot = main_pivot
    while difference > 0:
        ab_lst[pivot], ab_lst[pivot + 1] = ab_lst[pivot + 1], ab_lst[pivot]
        difference -= 1
        pivot += 1
        if pivot == n - 1:
            main_pivot -= 1
            pivot = main_pivot

    for char in ab_lst:
        print(char, end='')
