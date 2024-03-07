def solution(todo_list, finished):
    answer = dict(zip(todo_list, finished))
    return [key for key, val in answer.items() if val is False]