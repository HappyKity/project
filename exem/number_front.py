import number_back as nd
while True:
    print('1. 숫자추가\n2. 숫자출력\n999. 종료 ')
    select = int(input('메뉴 선택:'))

    if select == 1:
        num = int(input('숫자입력'))
        nd.save(num)
    elif select == 2:
        print(nd.find_all())
    elif select == 999:
        print('종료합니다.')
        break
