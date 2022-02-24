n, k = map(int, input().split())

arr = list(map(int, input().split()))

result = sum(arr[0:k])
temp = sum(arr[0:k])

for i in range(n-k):
    temp = temp - arr[i] + arr[k+i]
    if temp > result:
        result = temp

print(result)