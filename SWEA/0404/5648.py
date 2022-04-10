def move(direction):
    if direction == 0:
        dx, dy = 0, 1
    elif direction == 1:
        dx, dy = 0, -1
    elif direction == 2:
        dx, dy = -1, 0
    else:  # 3
        dx, dy = 1, 0

    return dx, dy


test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input())
    atom_list = []
    for _ in range(n):
        x, y, d, k = map(int, input().split())
        # 맵을 2000*2000으로봄(0.5초 단위로 생각하기 위해)
        atom_list.append([2*x, 2*y, d, k])
    atom_list.sort(key=lambda i: (i[0], i[1]))
    ans = 0

    while atom_list:
        atom_len = len(atom_list)
        for i in range(atom_len):
            dx, dy = move(atom_list[i][2])
            atom_list[i][0] += dx
            atom_list[i][1] += dy
            if -2000 <= atom_list[i][0] <= 2000 and -2000 <= atom_list[i][1] <= 2000:
                continue
            else:
                atom_list[i][2] = 5  # 범위 나가버림을 방향으로 표시

        # 충돌및 범위 탈출 계산
        atom_list.sort(key=lambda i: (i[0], i[1]))
        new_atom_list = []
        i = 0
        while i < atom_len:
            if atom_list[i][2] == 5:
                i += 1
                continue
            else:
                cnt = 1
                temp = atom_list[i][3]  # 에너지
                j = i + 1
                while j < atom_len:
                    if atom_list[i][0] == atom_list[j][0] and atom_list[i][1] == atom_list[j][1]:
                        cnt += 1
                        temp += atom_list[j][3]
                        j += 1
                    else:
                        break
                if cnt == 1:  # 같은게 없다면
                    new_atom_list.append(atom_list[i])
                    i += 1
                else:  # 같은게 있었다면
                    ans += temp  # 에너지 더해주고 리스트에서 제외
                    i = j

        atom_list = new_atom_list  # 바꿔줌

    print(f'#{tc} {ans}')