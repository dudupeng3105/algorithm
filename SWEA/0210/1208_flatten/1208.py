import sys

sys.stdin = open("input.txt")

for tc in range(10):
    dump_chance = int(input())
    given_list = list(map(int, input().split()))
    # 높이, 개수 리스트
    box_list = [0 for x in range(101)]  # 높이 0~100
    for box_height in given_list:
        box_list[box_height] += 1

    # 시작할 지점 찾기
    # 최대 높이 highest 구하기
    for height in range(100, 0, -1):  # 거꾸로 찾음
        if box_list[height]:  # 값이 있으면 highest
            highest = height
            break
    # 최소 높이 lowest 구하기
    for height in range(0, 101, 1):  # 순방향 찾음
        if box_list[height]:  # 값이 있으면 lowest
            lowest = height
            break

    for chance in range(dump_chance):  # 정해진 횟수만큼 시행
        # 먼저 가장 높은거 하나 뺌
        box_list[highest] -= 1
        box_list[highest - 1] += 1
        if box_list[highest] == 0:
            highest -= 1  # 이제 제일 높은 상자가 없으면 높이 한칸 내림

        # 젤 낮은거에 붙혀줌
        box_list[lowest] -= 1
        box_list[lowest + 1] += 1
        if box_list[lowest] == 0:
            lowest += 1  # 마찬가지로 없으면 올려줌

    # 최종 가장 높은 높이 - 가장 낮은 높이
    print(f'#{tc + 1} {highest - lowest}')
