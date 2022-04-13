a = '0' + input()
b = '0' + input()

a_len = len(a)
b_len = len(b)

arr = [[0 for _ in range(a_len)] for __ in range(b_len)]

for b_idx in range(1, b_len):
    arr[b_idx][0] = 0
    b_char = b[b_idx]
    for a_idx in range(a_len):
        if a[a_idx] == b_char:
            arr[b_idx][a_idx] = arr[b_idx - 1][a_idx - 1] + 1
        else:  # a[a_idx] != b_char
            arr[b_idx][a_idx] = max(arr[b_idx][a_idx - 1], arr[b_idx - 1][a_idx])

print(max(arr[b_len-1][:]))


# a=str(input())
# b=str(input())
#
# dp=[0]*len(b)
# for idx,el in enumerate(a):
# 	cnt=0
# 	for j in range(len(b)):
# 		if dp[j]>cnt:
# 			cnt=dp[j]
# 		elif el==b[j]:
# 			dp[j]=cnt+1
#
# print(max(dp))