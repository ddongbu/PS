def solution(name, yearning, photo):
    answer = []
    #사진별로 추억 점수 매긴다.
    
    #인물들의 그리움 점수를 모두 합산 = 추억점수
    
    #그리워하는 사람의 이름의 문자열 배열 = name
    #각 사람별 그리움 점수를 담은 정수 배열 = yearning
    #각 사진에 찍힌 인물의 이름을 담은 이차원 문자열 배열 photo
    
    #각 사진이 찍힌 이차원 배열인 photo를 보고 그리움 점수를 합산
    #[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"]]
    # = 19 , 15
    name_score = dict(zip(name,yearning))
    
    for people in photo:
        photo_sum = 0
        for name in people:
            photo_sum += name_score.get(name,0)
        answer.append(photo_sum)
    return answer