
# todos = [
#     {'tno': 1, 'title': '자바공부', 'finish': False},
#     {'tno': 2, 'title': 'python공부', 'finish': False}

# ]

# while True:
#     print('1.추가 2.변경 3.삭제 4.삭제2 999.삭제')
#     select_num = int(input('메뉴를 선택해주세요'))
#     if select_num == 1:
#         print('일정추가를 선택하셨습니다.')
#         title = input('추가할 일정을 작성해주세요')
#         tno = max(todo['tno']for todo in todos)
#         todo = {'tno':tno+1, 'title' : title, 'finish': False}
#         todos.append(todo)
#         print('추가를 완료했습니다.')
#     elif select_num == 2:
#         print('일정변경을 선택하셨습니다.')
#         for todo in todos :
#             print(todo)
#         select_update = int(input('변경할 일정을 골라주세요'))
#         if max(todo['tno']for todo in todos)>= select_update :
#             print('일정을 변경합니다')
#             todos[select_update-1]['finish']=True
#         else :
#             print('잘못선택하셨습니다.')
#     elif select_num == 3:
#         print('일정삭제를 선택하셨습니다.')
#         for todo in todos :
#             print(todo)
#         select_delete = int(input('삭제할 일정을 골라주세요'))
#         if max(todo['tno']for todo in todos)>= select_delete :
#             print('일정을 삭제합니다')
#             del todos[select_delete-1]
#         else :
#             print('잘못선택하셨습니다.')
#     elif select_num == 4:
#         print('일정삭제를 선택하셨습니다.')
#         for todo in todos :
#             print(todo)
#         select_delete2 = int(input('삭제할 일정을 골라주세요'))
#         if max(todo['tno']for todo in todos)>= select_delete2 :
#             for todo in todos:
#                 if todo['tno']== select_delete2-1 :
#                     todos.remove(todo)
#                     break
#         else :
#             print('잘못선택하셨습니다.')
#     elif select_num == 999:
#         print('종료합니다.')
#         break
#     else:
#         print('잘못입력하셨습니다 다시시도해주세요')

#chat gpt 최적화

todos = [
    {'tno': 1, 'title': '자바공부', 'finish': False},
    {'tno': 2, 'title': 'python공부', 'finish': False}
]

def print_todos():
    for todo in todos:
        print(todo)

while True:
    print('1.추가 2.변경 3.삭제 4.삭제2 999.종료')
    select_num = int(input('메뉴를 선택해주세요'))

    if select_num == 1:
        print('일정추가를 선택하셨습니다.')
        title = input('추가할 일정을 작성해주세요')
        tno = max(todo['tno'] for todo in todos)
        todo = {'tno': tno + 1, 'title': title, 'finish': False}
        todos.append(todo)
        print('추가를 완료했습니다.')

    elif select_num == 2:
        print('일정변경을 선택하셨습니다.')
        print_todos()
        select_update = int(input('변경할 일정을 골라주세요'))

        if 1 <= select_update <= len(todos):
            print('일정을 변경합니다')
            todos[select_update - 1]['finish'] = True
        else:
            print('잘못선택하셨습니다.')

    elif select_num == 3:
        print('일정삭제를 선택하셨습니다.')
        print_todos()
        select_delete = int(input('삭제할 일정을 골라주세요'))

        if 1 <= select_delete <= len(todos):
            print('일정을 삭제합니다')
            del todos[select_delete - 1]
        else:
            print('잘못선택하셨습니다.')

    elif select_num == 4:
        print('일정삭제를 선택하셨습니다.')
        print_todos()
        select_delete2 = int(input('삭제할 일정을 골라주세요'))

        if 1 <= select_delete2 <= len(todos):
            for todo in todos:
                if todo['tno'] == select_delete2:
                    todos.remove(todo)
                    break
        else:
            print('잘못선택하셨습니다.')

    elif select_num == 999:
        print('종료합니다.')
        break

    else:
        print('잘못입력하셨습니다 다시시도해주세요')

