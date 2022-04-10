given_string = list(map(str, input().split('-')))

ans = 0
for i in range(len(given_string)):
    nums = list(map(int, given_string[i].split('+')))
    if i == 0:
        ans = sum(nums)
    else:
        ans -= sum(nums)
print(ans)

