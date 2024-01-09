def 제곱(a):
    print(a*a)


제곱(10)
제곱(100)

numbers = [1, 5, 7]

for item in numbers:
    제곱(item)

# 정수 2개를 인자로 받아 덧셈 후 출력하는 함수를 정의하고 호출하시오


def 덧셈(a: int | float, b: int | float):
    c = a+b
    print(c)


덧셈(9.5, 10)

def hap2(a:int|float,b:int|float):
    #return 결과 -> 함수를 종료하고 결과로 바꿔라
    return a+b

hap2(3,4)

result = hap2(3,4)

print(result)