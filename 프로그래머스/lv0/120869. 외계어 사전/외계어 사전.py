def solution(spell, dic):
    for i in dic:
        if sorted(list(i)) == sorted(spell):
            return 1
    return 2