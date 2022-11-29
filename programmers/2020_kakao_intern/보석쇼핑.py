def solution(gems):
    num_type = len(set(gems))
    gems_len = len(gems)
    s = 0
    e = 0
    temp = 1000001
    jewel_box = {gems[0]: 1}
    answer = []
    while s <= e < gems_len:
        jewel_num_type = len(jewel_box)
        # print(s, e, jewel_box)
        if num_type == jewel_num_type:
            temp_len = e + 1 - s
            if temp_len < temp:
                temp = temp_len
                # print(s, e, jewel_box, temp)
                answer = [s + 1, e + 1]

            jewel_box[gems[s]] -= 1
            if not jewel_box[gems[s]]:
                del jewel_box[gems[s]]
            s += 1
        else:  # jewel_num_type < num_type:
            e += 1
            if e == gems_len:
                break
            jewel_box[gems[e]] = jewel_box.get(gems[e], 0) + 1

    print(answer)
    return answer


solution(	["AA", "AB", "AC", "AA", "AC"])
