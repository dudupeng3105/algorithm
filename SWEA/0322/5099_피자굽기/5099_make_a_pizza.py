from collections import deque


test_case = int(input())
for tc in range(1, test_case + 1):
    # n 화덕 크기, m 총 넣어야 하는 피자
    n, m = map(int, input().split())
    pizza_q = deque(list(map(int, input().split())))
    pizza_oven = [[] for _ in range(n)]

    rotation_num = 0
    cnt = 1
    total_pizza = 0
    while rotation_num < n or total_pizza != 1:
        oven_slot = rotation_num % n
        if not pizza_oven[oven_slot]:
            if pizza_q:
                cheese = pizza_q.popleft()
                pizza_oven[oven_slot] = [cnt, cheese]
                cnt += 1
                total_pizza += 1
        else: # 자리에 피자 있으면
            pizza_oven[oven_slot][1] = pizza_oven[oven_slot][1]//2
            if pizza_oven[oven_slot][1] == 0:  # 치즈 다 녹으면
                if pizza_q:  # q가 남아있으면 새 피자 넣어줌
                    cheese = pizza_q.popleft()
                    pizza_oven[oven_slot] = [cnt, cheese]
                    cnt += 1
                else:
                    pizza_oven[oven_slot] = []
                    rotation_num += 1
                    total_pizza -= 1
                    continue

        print(pizza_oven)
        rotation_num += 1

    for slot in pizza_oven:
        if slot:
            print(f'#{tc} {slot[0]}')
            break