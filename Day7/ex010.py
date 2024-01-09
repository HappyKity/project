import ex009


def print_menu():
    print('메뉴를 골라주세요\n1.값추가 2.값확인 3.값변환 4.값삭제 999.종료')


def input_select():
    return input('값을 입력해주세요')


def add_value():
    a = input('추가할 값을 입력해주세요')
    ex009.numbers.append(a)


def list_numbers():
    print('값출력')
    print(ex009.numbers)


def change_number():
    print('값변경')
    print(ex009.numbers)
    update_num = int(input('변경할 값의 순서를 입력해주세요'))
    new_num = input('변경할 값을 입력해주세요')
    
    
    if 0 <= update_num < len(ex009.numbers):
        ex009.numbers[update_num-1] = new_num
        print('변경이 완료되었습니다.')
    else:
        print('값을 잘못입력하셨습니다.')


def delete_number():
    print('값삭제')
    print(ex009.numbers)
    delete_num = input('삭제할 값을 입력해주세요')
    if delete_num in ex009.numbers:
        ex009.numbers.remove(delete_num)
        print('삭제가 완료되었습니다.')
    else:
        print('값을 잘못입력하셨습니다.')



def end_program():
    print('종료합니다.')
