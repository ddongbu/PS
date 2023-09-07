def solution(s):
    answer = []
    words = s.split(" ")
    for word in words:
        w=""
        for i in range(len(word)):
            if i % 2 == 0:
                w += word[i].upper()
            else:
                w += word[i].lower()
        answer.append(w)
    return ' '.join(answer)