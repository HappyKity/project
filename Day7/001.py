# 웹 프로그래밍
# 데이터 1건 : dictionary
# 관리자가 한명이면 변수로 지정하면 그만이다.
# 관리자 아이디, 관리자 비밀번호
admin_id = 'admin'
admin_pw = '0000'

# 여러건 : list
{"아이디": 'spring', '나이': 25, '성인여부': True}

book = {'번호': '001', '제목': '이것이 자바다', '작가': '신용권', '가격': 32400, '출판일': '2022-09-05'}

# 키와 값의 pair로 정보를 표현 -> 딕셔너리
products = [
    {'번호': 1, '이름': '코카콜라', '가격': 2000, '재고': 20},
    {'번호': 2, '이름': '팹시콜라', '가격': 1900, '재고': 10}
]
print(products[0]['이름'])
