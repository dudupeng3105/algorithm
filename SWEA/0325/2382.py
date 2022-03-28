test_case = int(input())


def displacement(d):
    if d == 1:  # 상
        return -1, 0
    elif d == 2: # 하
        return 1, 0
    elif d == 3: # 좌
        return 0, -1
    else:  # d == 4:  우
        return 0, 1


def changed_direction(d):
    if d == 1:  # 상
        return 2
    elif d == 2:  # 하
        return 1
    elif d == 3:  # 좌
        return 4
    else:  # d == 4:  우
        return 3


def merge_microbe(a_lst):
    cnt = 0
    i = 0
    while i < len(a_lst) - 1:
        if a_lst[i][0] == a_lst[i+1][0] and a_lst[i][1] == a_lst[i+1][1]:
            cnt += 1
            i += 1
        else:
            if cnt:  # 같은 좌표가 있을 때
                merge_population = 0
                max_population = 0
                merge_direction = 0
                for temp in a_lst[i-cnt:i+1]:
                    if temp[2] > max_population:
                        max_population = temp[2]
                        merge_direction = temp[3]

                    merge_population += temp[2]
                # 다수를 한 개로 합치기
                a_lst = a_lst[:i-cnt] + [[temp[0], temp[1], merge_population, merge_direction]] + a_lst[i+1:]
                i = i-cnt+1
                cnt = 0
            else:
                i += 1
                continue

    return a_lst


for tc in range(1, test_case + 1):
    n, m, k = map(int, input().split())
    microbe_lst = []
    for _ in range(k):
        r, c, population, direction = map(int, input().split())
        microbe_lst.append([r,c, population, direction])

    for _ in range(m):
        for microbe in microbe_lst:
            population, direction = microbe[2:]
            dr, dc = displacement(direction)
            microbe[0] += dr
            microbe[1] += dc
            # 레드존
            if microbe[0] == 0 or microbe[0] == n-1 or \
                    microbe[1] == 0 or microbe[1] == n-1:
                microbe[2] = microbe[2] // 2
                microbe[3] = changed_direction(direction)
                if microbe[2] == 0:  # 미생물 수 0 이면 삭제
                    microbe_lst.remove(microbe)
            else:
                continue

        microbe_lst.sort(key=lambda x: (x[0], x[1]))
        microbe_lst = merge_microbe(microbe_lst)


    #print(microbe_lst)
    # 미생물 수 구하기
    ans = 0
    for microbe in microbe_lst:
        ans += microbe[2]

    print(f'#{tc} {ans}')

