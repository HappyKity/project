# 할일은 할일번호, 할일, 완료여부로 구성
todos = []
todos.append({'tno': 1, 'title': '자바공부', 'finish': False})
todos.append({'tno': 2, 'title': '스프링공부', 'finish': False})
todos.append({'tno': 3, 'title': '파이썬 공부', 'finish': False})
print(todos)


def menu():
    print('할일관리')
    print('1. 할일 목록\n2.할일 추가\n3.할일 변경\n4.삭제\n5. 완료율\n999.종료')


def print_list():
    for item in todos:
        print(item)


def insert_list():
    print('할일 추가를 선택하셨습니다')
    insert_user = input('추가할 할일을 적어주세요 :')
    max_tno = max(todo['tno'] for todo in todos)
    todos.append({'tno': max_tno+1, 'title': insert_user, 'finish': False})


def update_list():
    print('할일 변경을 선택하셨습니다.')
    for item in todos:
        print(item)
    update_user = int(input('변경할 할일의 번호를 입력해주세요:'))
    if max(todo['tno']for todo in todos) >= update_user:
        print(update_user)
        for item in todos:
            if item['tno'] == update_user:
                if item['finish'] == False:
                    item['finish'] = True
                    print_list()
                    print('변경이 완료 되었습니다.')
                elif item['finish'] == True:
                    item['finish'] = False
                    print_list()
                    print('변경이 완료 되었습니다.')
                else:
                    print('오류입니다. 관리자에게 문의하세요')
    else:
        print('잘못입력하셨습니다. 다시시도해주세요')


def delete_list():
    print('할일 삭제을 선택하셨습니다.')
    for item in todos:
        print(item)
    update_user = int(input('삭제할 할일의 번호를 입력해주세요:'))
    if max(todo['tno']for todo in todos) >= update_user:
        print(update_user)
        for item in todos:
            if item['tno'] == update_user:
                del todos[update_user-1]
                print('삭제가 완료 되었습니다.')
            if item['tno'] > update_user:
                for optimization_list in todos:
                    optimization_list['tno'] = optimization_list['tno']-1
                print_list()
    else:
        print('잘못입력하셨습니다. 다시시도해주세요')


while True:
    menu()
    select = int(input('메뉴를 선택해주세요:'))
    if select == 1:
        print_list()
    elif select == 2:
        insert_list()
    elif select == 3:
        update_list()
    elif select == 4:
        delete_list()
    elif select == 5:
        avg_todos()
    elif select == 999:
        print('종료합니다.')
        break
    else:
        print('잘못입력하셨습니다. 다시입력해주세요')
