def solution(s):
    s=s.lower()
    if s.count('p')!=s.count('y'):
        print('false')
    else:
        print('true')

    return False if s.count('p')!=s.count('y') else True
