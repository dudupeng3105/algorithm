from math import ceil
n = int(input())
room_lst = list(map(int, input().split()))
b, c = map(int, input().split())

total = 0
for room in room_lst:
    room -= b
    total += 1
    if room > 0:
        total += ceil(room/c)

print(total)