import sys

input = sys.stdin.readline

A, B = map(int, input().split())
N, M = map(int, input().split())
robots_pos = [[0, 0, "E"] for _ in range(N + 1)]
pos_set = set()
rotate_dict = {"N": 0, "W": 3, "E": 1, "S": 2}
rotate_dict_inverse = {0: "N", 1: "E", 2: "S", 3: "W"}
rotate_displacement = {"N": (-1, 0), "W": (0, -1), "E": (0, 1), "S": (1, 0)}

for i in range(N):
    x, y, head = map(str, input().split())
    x, y = int(x) - 1, B - int(y)
    robots_pos[i + 1] = [y, x, head]
    pos_set.add((y, x))


# 명령수행
flag = False
for j in range(M):
    # print(j, robots_pos)
    robot_num, op, op_iter_num = map(str, input().split())
    robot_num, op_iter_num = int(robot_num), int(op_iter_num)
    if op == 'L':  # 왼쪽 90도 회전
        # 0 + 3 = 3
        cnt = op_iter_num % 4
        while cnt:
            # print("다음방향", rotate_dict_inverse[(rotate_dict[robots_pos[robot_num][2]] + 3) % 4])
            robots_pos[robot_num][2] = rotate_dict_inverse[(rotate_dict[robots_pos[robot_num][2]] + 3) % 4]
            cnt -= 1
    elif op == 'R':  # 오른쪽 90도 회전
        cnt = op_iter_num % 4
        while cnt:
            robots_pos[robot_num][2] = rotate_dict_inverse[(rotate_dict[robots_pos[robot_num][2]] + 1) % 4]
            cnt -= 1

    else:  # op == 'F' 전진
        cnt = op_iter_num
        o_r, o_c = robots_pos[robot_num][0], robots_pos[robot_num][1]
        n_r, n_c = o_r, o_c
        head_direction = robots_pos[robot_num][2]
        dr, dc = rotate_displacement[head_direction]
        while cnt:
            cnt -= 1
            n_r, n_c = n_r + dr, n_c + dc
            if 0 <= n_r < B and 0 <= n_c < A:
                if (n_r, n_c) in pos_set: # 다른 로봇이 있어요
                    # 부딪힌 로봇 찾기
                    for k in range(1, N+1):
                        if robots_pos[k][0] == n_r and robots_pos[k][1] == n_c:
                            print(f'Robot {robot_num} crashes into robot {k}')
                            flag = True
                            break

                    if flag:
                        break

            else: # 벽 밖으로 나가버림
                print(f'Robot {robot_num} crashes into the wall')
                flag = True
                break

        pos_set.remove((o_r, o_c))
        pos_set.add((n_r, n_c))
        robots_pos[robot_num][0], robots_pos[robot_num][1] = n_r, n_c

    if flag:
        break

if not flag:
    print("OK")