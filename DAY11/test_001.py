# 숫자를 제곱하는 함수
def count_num(num: int) -> int:
    # int가 아니면 실패 -> int는 어떻게 아는가? 실패는 뭐지
    # 타입을 비교하는 경우에는 isinstance를 쓰면 된다.
    # isinstance(값, 타입) == Ture,False 골라서 넣는
    if isinstance(num, int) == False:
        return -1
    return num*num
