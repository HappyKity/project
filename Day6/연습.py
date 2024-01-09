num1, num2 = 10, 3.14
print(f'덧셈{num1+num2}, 뺄셈{num1-num2}, 곱셈{num1*num2}, 나눗셈{num1/num2}')
# 여기서 f는 format

# 절대값 함수 abs
print(abs(100))
print(abs(-100))
print(abs(num1))

str = "0123456789"
# 홀수만 출력
print(str[1::2])
# 3의 배수만 출력
print(str[0::3])
print(str[::3]) # 어차피 처음부터라 0안써도 됨