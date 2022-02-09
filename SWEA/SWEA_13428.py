# 9자리 이하, 음이 아닌 정수 N
# 위치를 바꾸는 일을 한번이나 0번하여
# 새로운 수 M, 맨 앞자리 0이면 안됨
# M의 최솟값 최댓값을 구하라
def find_min(N, num_length):
    result = N.copy()
    for i in range(num_length):
        for j in range(i + 1, num_length):
            if i == 0 and N[j] == 0:
                continue            
            if N[i] <= N[j]:
                continue
            else:
                N[i], N[j] = N[j], N[i]
                #print(N)
                for k in range(num_length):
                    if result[k] == N[k]:
                        continue
                    elif result[k] < N[k]:
                        break
                    else:
                        result = N.copy()
                        break   
                N[i], N[j] = N[j], N[i]
                #print(N)

    return result


def find_max(N, num_length):
    result_max = N.copy()
    for i in range(num_length):
        for j in range(i + 1, num_length):
            if i == 0 and N[j] == 0:
                continue
            if N[i] >= N[j] or N[j] == 0:
                continue
            else:
                N[i], N[j] = N[j], N[i]
                for k in range(num_length):
                    if result_max[k] == N[k]:
                        continue
                    elif result_max[k] > N[k]:
                        break
                    else:
                        result_max = N.copy()
                        break   
                N[i], N[j] = N[j], N[i]

    return result_max


testcase = int(input())
for tc in range(testcase):
    N = list(map(int, input()))
    if N[0] == 0:
        print(f'#{tc+1} {0} {0}')
        continue
    num_length = len(N)
    r1 = "".join(map(str, find_min(N, num_length)))
    r2 = "".join(map(str, find_max(N, num_length)))
    print(f'#{tc+1} {r1} {r2}')    