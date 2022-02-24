n = int(input())
number = list(map(int, input().split()))
line = [0]

for i in range(1, n+1):
    num = i - number[i-1]
    # 슬라이싱은 범위 벗어나면 [] 리턴임
    line = line[:num] + [i] + line[num:]
print(*line[1:])

