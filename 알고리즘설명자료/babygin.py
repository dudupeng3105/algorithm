import sys
sys.stdin = open("test.txt")

test_case = int(input())
for tc in range(1, test_case + 1):
    card_list = list(map(int, input()))
    print(card_list)
    num_list = [0 for x in range(10)]
    for num in card_list:
        num_list[num] += 1

    cnt = 0
    # triplet 확인
    for i in range(10):
        if num_list[i] >= 3:
            cnt += 1
            num_list[i] -= 3
            if num_list[i] == 3: # 6일 경우
                cnt+=1
                num_list[i] -= 3

    # 런 확인
    for i in range(8):
        if num_list[i] and num_list[i+1] and num_list[i+2]:
            if num_list[i] == num_list[i+1] == num_list[i+2] == 2:
                cnt += 2
                num_list[i] -= 2
                num_list[i + 1] -= 2
                num_list[i + 2] -= 2
            else:
                cnt += 1
                num_list[i] -= 1
                num_list[i + 1] -= 1
                num_list[i + 2] -= 1

    if cnt == 2:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')
