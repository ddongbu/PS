def solution(score):
    answer = []
    sort_scores = []
    scores = [sum(i)/len(i) for i in score] #평균 리스트
    sort_scores = sorted(scores,reverse=True) #순위 구할때 이용
    
    for i in scores:
        answer.append(sort_scores.index(i)+1)

    return answer