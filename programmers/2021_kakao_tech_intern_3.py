def solution(n, k, cmd):
    doubly_linked_list = {x: [x - 1, x + 1] for x in range(n)}
    doubly_linked_list[0] = [None, 1]
    doubly_linked_list[n - 1] = [n - 2, None]
    delete_history = []
    now_selected = k
    live_table = ['O' for _ in range(n)]

    for op in cmd:
        # print(now_selected, op, doubly_linked_list, live_table)
        if op[0] == 'D':
            dist = int(op[2:])
            for _ in range(dist):
                now_selected = doubly_linked_list[now_selected][1]

        elif op[0] == 'U':
            dist = int(op[2:])
            for _ in range(dist):
                now_selected = doubly_linked_list[now_selected][0]

        elif op[0] == 'C':
            live_table[now_selected] = 'X'
            prev, next = doubly_linked_list[now_selected]
            delete_history.append([prev, now_selected, next])
            if next == None:
                now_selected = doubly_linked_list[now_selected][0]  # up
            else:
                now_selected = doubly_linked_list[now_selected][1]  # down
            if prev == None:
                doubly_linked_list[next][0] = None
            elif next == None:
                doubly_linked_list[prev][1] = None
            else:
                doubly_linked_list[next][0] = prev
                doubly_linked_list[prev][1] = next

        else:  # Z, 복구
            prev, now, next = delete_history.pop()
            live_table[now] = 'O'  # 살리고 up, down 다시 찾음
            if prev == None:
                doubly_linked_list[next][0] = now
            elif next == None:
                doubly_linked_list[prev][1] = now
            else:
                doubly_linked_list[next][0] = now
                doubly_linked_list[prev][1] = now

    answer = ''.join(live_table)
    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
