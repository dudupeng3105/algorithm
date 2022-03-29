test_case = int(input())


for tc in range(1, test_case + 1):
    n, m = map(int, input().split())
    load_lst = list(map(int, input().split()))
    truck_lst = list(map(int, input().split()))
    load_lst.sort(reverse=True)
    truck_lst.sort(reverse=True)
    print(load_lst)
    print(truck_lst)

    len_truck = len(truck_lst)
    len_load = len(load_lst)
    t_i = 0  # truck_index
    l_i = 0  # load_index
    ans_weight = 0
    while t_i < len_truck and l_i < len_load:
        if truck_lst[t_i] >= load_lst[l_i]:  # 트럭이 실을 수 있으면
            ans_weight += load_lst[l_i]
            t_i += 1
            l_i += 1
        else:  # 현재 트럭이 실을 수 없으면 다음 짐(load)을 알아봄
            l_i += 1

    print(f'#{tc} {ans_weight}')
