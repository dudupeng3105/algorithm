import sys

sys.stdin = open("test.txt")

test_case = int(input())
for tc in range(1, test_case + 1):
    room_cnt = [0 for x in range(401)]
    student_num = int(input())
    for _ in range(student_num):
        room_a, room_b = map(int, input().split())
        # 넘버가 큰방부터 입력이 들어올 수도 있음
        if room_a > room_b:
            end_room = room_a
            start_room = room_b
        else:
            start_room = room_a
            end_room = room_b
        # 시작하는 방이 3과 4인 경우는 같으므로
        # 시작하는 방이 짝수면 1 빼줌
        if start_room % 2 == 0:  # 짝수이면
            start_room = start_room - 1
        # 종료하는 방이 9과 10인 경우는 같으므로
        # 종료하는 방이 홀수면 1 더해줌
        if end_room % 2 == 1:  # 홀수 이면
            end_room = end_room + 1

        # start~end 룸까지 1씩 cnt
        for i in range(start_room, end_room+1):
            room_cnt[i] += 1

    # 최대값 구하기
    max_time = max(room_cnt)
    print(f'#{tc} {max_time}')