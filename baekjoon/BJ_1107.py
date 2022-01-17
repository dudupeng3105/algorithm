def checker(num):
    num = list(str(num))
    for i in num:
        if i in broken_button_list:
            return False
    return True


want_channel = int(input())
broken_button_num = int(input())
if broken_button_num != 0:
    broken_button_list = list(input().split(" "))
else:  # 고장난 버튼 없을 때
    broken_button_list = []

result = abs(want_channel - 100)

for i in range(1000001):
    if checker(i):
        result = min(result, len(str(i)) + abs(i - want_channel))
print(result)