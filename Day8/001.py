# 나이를 입력받아 성년 또는 미성년을 리턴하는 함수

age = int(input('나이를 입력해주세요'))

if age >= 18:
    print('성인입니다.')
else:
    print('미성년입니다.')


def adult_check(age):
    if age >= 18:
        return True
    else:
        return False


if adult_check(age) == True:
    print('당신은 출입가능합니다.')
else:
    print('당신은 출입이 불가능합니다.')

# 두 숫자를 입력받아 큰수를 가리는 함수

first_num = int(input('첫번째 수를 입력해주세요'))
secound_num = int(input('두번째 수를 입력해주세요'))


def count_num(first_num, secound_num):
    if first_num > secound_num:
        return 1
    elif secound_num > first_num:
        return 2
    else:
        return 0


if count_num(first_num, secound_num) == 1:
    print(f'큰수는 첫번째 수인 {first_num}입니다')
elif count_num(first_num, secound_num) == 2:
    print(f'큰수는 두번째 수인 {secound_num}입니다')
elif count_num(first_num, secound_num) == 0:
    print('두 수는 같은 수입니다')
else:
    print('이건 오류다')

# 숫자를 입력받아 절대값을 게산하는 함수
numbers = int(input('숫자를 입력해주세요'))

def number_count(numbers):
    if numbers >= 0:
        return numbers
    elif numbers < 0:
        return -numbers


print(f"절대값은 {number_count(numbers)}입니다.")