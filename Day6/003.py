# 숫자를 입력받아  CR(합계, 평균) UD
# 메뉴를 띄운다(1 : 숫자 추가 2 : 숫자 출력 3 : 입력수 합계 4 : 입력수 평균 999 : 종료)


numbers = []

while True:
    select_num = input(
        '숫자를 선택해주세요\n1.숫자추가\n2.숫자출력\n3.입력수 합계\n4.입력수 평균\n5.입력값 순서로 삭제\n6.입력값 지정 삭제\n999.종료\n')
    if select_num == '1':
        update_num = int(input('추가할 숫자를 입력해주세요'))
        numbers.append(update_num)
    elif select_num == '2':
        print(f'지금까지 추가된 수는 {numbers}입니다.')
    elif select_num == '3':
        total_num = 0
        for x in numbers:
            total_num += x
        print(f'지금까지 입력된 수의 합계는 {total_num}입니다.')
    elif select_num == '4':
        totla_avgnum = 0
        for x in numbers:
            totla_avgnum += x
        avg_num = totla_avgnum/len(numbers)
        print(f'지금까지 입력된 수의 평균는 {avg_num}입니다.')
    elif select_num == '5':
        print(f'입력하신 숫자는 {numbers}입니다.')
        del_num = int(input('삭제할 숫자의 순서를 입력해주세요'))
        del numbers[del_num-1]
        print(f'삭제를 완료했습니다.\n지금 남아있는 입력하신 수는 {numbers}입니다.')
    elif select_num == '6':
        print(f'입력하신 숫자는 {numbers}입니다.')
        del_nums = int(input('삭제할 숫자를 입력해주세요'))
        if del_nums in numbers:
            numbers.remove(del_nums)
            print(f'삭제를 완료했습니다.\n지금 남아있는 입력하신 수는 {numbers}입니다.')
        else :
            print('없는 값을 입력하셨습니다. 다시 시도해주세요')
    elif select_num == '999':
        print('종료합니다.')
        break
    else:
        print('항목을 자세히 보고 선택해주세요!!')
