def baby_gin():
    flag = 0
    for i in range(12):
        card_num = card_lst[i]
        if not i % 2:  # a 차례
            a_cnt[card_num] += 1
            # triplet 체크
            if a_cnt[card_num] == 3:
                flag = 1
                return flag
            # 런 체크
            cnt = 0
            for card_cnt in a_cnt:
                if card_cnt:
                    cnt += 1
                    if cnt == 3:
                        flag = 1
                        print(a_cnt)
                        return flag
                else:
                    cnt = 0

        else:  # b 차례
            b_cnt[card_num] += 1
            # triplet 체크
            if b_cnt[card_num] == 3:
                flag = 2
                return flag
            # 런 체크
            cnt = 0
            for card_cnt in b_cnt:
                if card_cnt:
                    cnt += 1
                    if cnt == 3:
                        flag = 2
                        print(b_cnt)
                        return flag
                else:
                    cnt = 0

    return flag


test_case = int(input())
for tc in range(1, test_case + 1):
    card_lst = list(map(int, input().split()))
    a_cnt = [0 for _ in range(10)]
    b_cnt = [0 for _ in range(10)]

    ans = baby_gin()
    print(f'#{tc} {ans}')
