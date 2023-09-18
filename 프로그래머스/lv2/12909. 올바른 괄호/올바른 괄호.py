def solution(s):
    answer = True
    stack = []

    for i in s : # 요소를 차례대로 입력 # Ex : ()()
        if i == "(":
            stack.append(i)
            #1 append "("
            #3 append "("

        else: # ")"
            if stack == []:
                answer = False
                break
            else:
                stack.pop() # pop() : 인덱스 지정 안 되면, 맨 뒤 요소 pop 
                #2 pop "("
                #4 pop "("
    if stack != []:
        answer = False 
    # else:            
    return answer