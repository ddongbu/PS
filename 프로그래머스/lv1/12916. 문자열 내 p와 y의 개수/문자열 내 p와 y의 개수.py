def solution(s):
    s = s.lower()
    print(s)
    if s.count('y') == s.count('p'):
        return True
    else:
        return False