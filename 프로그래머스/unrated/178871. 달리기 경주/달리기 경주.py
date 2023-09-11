def solution(players, callings):
    # playerDict 선언 (key : 플레이어 이름, value : 플레이어 인덱스)
    playerDict = dict()
    #playerDict 초기화
    for idx, player in enumerate(players):
        playerDict[player] = idx
    # callings 배열 반복
    for player in callings:
        #앞지른 선수의 인덱스 
        idx = playerDict.get(player)
        # 뒤쳐진 선수의 이름
        frontPlayer = players[idx - 1]
        # 인덱스 수정
        playerDict[player] = idx - 1
        playerDict[frontPlayer] = idx
        
        players[idx - 1] = player
        players[idx] = frontPlayer
    return players