length = int(input())
arr = [0 for _ in range(length)]
arr = list(map(int, input().split()))
# 가장 긴 증가수열
longest = 1
temp = 1
for i in range(1, length):
    if arr[i] >= arr[i-1]:
        temp += 1
        if temp > longest:
            longest = temp
    else:
        temp = 1
# 가장 긴 감소수열
temp = 1
for i in range(1, length):
    if arr[i] <= arr[i-1]:
        temp += 1
        if temp > longest:
            longest = temp
    else:
        temp = 1

print(longest)