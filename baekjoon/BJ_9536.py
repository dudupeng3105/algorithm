test_case = int(input())
for test_case in range(test_case):
    wolf_howl = list(map(str, input().rstrip().split()))
    animal_howl = []
    while True:
        howl = list(map(str, input().rstrip().split()))
        if len(howl) > 3:
            break
        else:
            animal_howl.append(howl[2])

    result = []
    for w_howl in wolf_howl:
        if w_howl not in animal_howl:
            result.append(w_howl)

    print(*result)