def solution(s):
    answer = []
    #s는 알파벳과 숫자, 공백문자로 이루어져 있다.
    #숫자는 단어의 첫 문자로만 나온다.
    #숫자로만 이루어진 단어는 없다.
    #공백문자가 연속해서 나올 수 없다.
    #모든 단어의 첫 문자가 대문자이고 그 외의 알파벳은 소문자인 문자열
    words = s.split(" ")
    for char in words:
        if char != "":
            answer.append(char[0].upper() + char[1:].lower())
        else:
            answer.append("")
    return " ".join(answer)