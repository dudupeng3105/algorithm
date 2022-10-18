# R T
# C F
# J M
# A N


def solution(survey, choices):
    score_dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i in range(len(survey)):
        suv = survey[i]
        a, b = suv[0], suv[1]
        choice = choices[i]
        if choice < 4:
            score_dict[a] += (4-choice)
        else: # choice >=4
            score_dict[b] += (choice-4)

    rt = 'R' if score_dict['R'] >= score_dict['T'] else 'T'
    cf = 'C' if score_dict['C'] >= score_dict['F'] else 'F'
    jm = 'J' if score_dict['J'] >= score_dict['M'] else 'M'
    an = 'A' if score_dict['A'] >= score_dict['N'] else 'N'

    answer = rt + cf + jm + an
    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
print(solution(survey, choices))
