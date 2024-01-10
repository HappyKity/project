# 1부터 10까지의 합계

num = 0


for x in range(1, 11):
    num += x
print(num)

# 1에서 10까지의 3의 배수 출력

for x in range(1, 11):
    if x % 3 == 0:
        print(x)
# 반대로 할 수 있는 예재 : 사용처 회원가입시 프로필 사진을 업로드 했으면 저장 아니면 countinue
for x in range(1, 11):
    if x % 3 != 0:
        continue
    print(x)

#1에서 10사이의 3의 배수의 합계
value = 0
for x in range(1,11):
    if x%3 == 0:
        value += x
print(value)

#1에서 100 사이의 3과 5의 공배수를 구하시오

value = 0
for z in range(1,101):
    if z%5 == 0 or z%7 == 0:
        if z%5 == 0 and z%7 == 0:
            continue
        else:
            print(z)



