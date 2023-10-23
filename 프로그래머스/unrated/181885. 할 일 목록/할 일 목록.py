def solution(todo_list, finished):
    answer = []
    for idx,k in enumerate(finished):
        if k == False:
            answer.append(todo_list[idx])
    return answer