todos = [
    {'tno': 1, 'title': '자바공부', 'finish': False},
    {'tno': 2, 'title': 'python공부', 'finish': False}

]
print(todos)
# create

title = input('할일입력:')
# 배열안에 가장 큰수를 찾아 다음수로 자동 저장하는 코드
tno = max(todo['tno']for todo in todos)+1

todo = {'tno': tno, 'title': title, "finish": False}
todos.append(todo)
# Read : for로 todos 출력
# for todo in todos:
#    print(todo)

# update : tno로 찾아 finish를 변경
while True:
    for todo in todos:
        print(todo)
    print('3 : 일정삭제')

    print('종료하려면 999를 입력하세요')
    select_num = int(input('완료한 일정을 골라주세요'))
    if max(todo['tno']for todo in todos) >= select_num:
        todos[select_num-1]['finish'] = True
    elif select_num == 999:
        print('종료합니다.')
        break
    else:
        print('잘못입력하셨습니다.')
