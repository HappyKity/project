#정수변수를 2개 만들어, 나눗셈 결과를 출력하시오
#예외처리가 필요하면 예외 처리하시오
def count_num():
    try:
        first_num = int(input('첫번째 숫자를 입력해주세요'))
        secound_num = int(input('두전째 숫자를 입력해주세요'))
        return first_num/secound_num
    except:
        return None
        

print(count_num())