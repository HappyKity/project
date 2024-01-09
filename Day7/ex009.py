# 숫자 리스트 - 추가, 목록, 합계, 변경, 삭제. 함수버전
# def print_menu():
#     print('메뉴를 골라주세요\n1.값추가 2.값확인 3.값변환 4.값삭제 999.종료')


# def input_select():
#     return input('값을 입력해주세요')


# def add_value():
#     a = input('추가할 값을 입력해주세요')
#     numbers.append(a)


# def list_numbers():
#     print('값출력')
#     print(numbers)


# def change_number():
#     print('값변경')
#     print(numbers)
#     update_num = int(input('변경할 값의 순서를 입력해주세요'))
#     new_num = input('변경할 값을 입력해주세요')
    
    
#     if 0 <= update_num < len(numbers):
#         numbers[update_num-1] = new_num
#         print('변경이 완료되었습니다.')
#     else:
#         print('값을 잘못입력하셨습니다.')


# def delete_number():
#     print('값삭제')
#     print(numbers)
#     delete_num = input('삭제할 값을 입력해주세요')
#     if delete_num in numbers:
#         numbers.remove(delete_num)
#         print('삭제가 완료되었습니다.')
#     else:
#         print('값을 잘못입력하셨습니다.')



# def end_program():
#     print('종료합니다.')
import ex010
from ex010 import print_menu,input_select,add_value,list_numbers,change_number,delete_number,end_program

numbers = []
while True:
    print_menu()
    select = input_select()
    if select == '1':
        add_value()
    elif select == '2':
        list_numbers()
    elif select == '3':
        change_number()
    elif select == '4':
        delete_number()
    elif select == '999':
        end_program()
        break
