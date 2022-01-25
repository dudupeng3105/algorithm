N = int(input())
given_seq = list(map(int, input().split()))
prev_peak = 0
for i in range(N-1, 0, -1):
    if given_seq[i-1] < given_seq[i]:
        prev_peak = i - 1
        break

for i in range(N-1, 0, -1):
    if given_seq[prev_peak] < given_seq[i]:
        given_seq[prev_peak], given_seq[i] = given_seq[i], given_seq[prev_peak]
        given_seq = given_seq[:prev_peak+1] + sorted(given_seq[prev_peak+1:])
        print(*given_seq)
        exit()
print(-1)
