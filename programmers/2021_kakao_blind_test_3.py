def solution(info, query):
    n = len(info)
    lang_dict = {'java': set(), 'python': set(), 'cpp': set()}
    pos_dict = {'backend': set(), 'frontend': set()}
    career_dict = {'junior': set(), 'senior': set()}
    food_dict = {'pizza': set(), 'chicken': set()}
    score = [0]
    # dict 채우기
    for i in range(n):
        information = info[i]
        lang, pos, career, food, str_score = info[i].split(" ")
        # print(lang, pos, career, food, str_score)
        lang_dict[lang].add(i + 1)
        pos_dict[pos].add(i + 1)
        career_dict[career].add(i + 1)
        food_dict[food].add(i + 1)
        score.append(int(str_score))

    answer = []
    for q in query:
        temp = set([x for x in range(1, n + 1)])
        cnt = 0
        q_lang, q_pos, q_career, q_food_q_score = q.split(' and ')
        q_food, q_score = q_food_q_score.split(" ")
        q_score = int(q_score)
        if not q_lang == '-':
            temp = temp & lang_dict[q_lang]
        if not q_pos == '-':
            temp = temp & pos_dict[q_pos]
        if not q_career == '-':
            temp = temp & career_dict[q_career]
        if not q_food == '-':
            temp = temp & food_dict[q_food]

            # 점수 계산
        for idx in temp:
            if score[idx] >= q_score:
                cnt += 1

        answer.append(cnt)

    return answer