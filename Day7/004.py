#할일관리
todos = [
    {'tno':1,'title':'할일1','reg_day':'2024-01-09','finish':True},
    {'tno':2,'title':'할일2','reg_day':'2024-01-09','finish':True}
]
tno = 2
#Read : 전체읽기, 1개 읽기


for todo in todos:
    print(todo)
# 할일 번호를 입력받아 찾아서 출력
find = False
select_num = int(input('선택할 할 일을 입력해주세요'))
for todo in todos :
    if todo['tno']==select_num:
        print(todo)
        find = True
        break
if find == False :
    print('굳이 이렇게 작성하능 이유가 무엇인가.')
    