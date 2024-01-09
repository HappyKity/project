numbers = [1, 3, 5, 7]

# 그 숫자가 numbers에 있는지(True/False) 출력
num = 5          
print(num in numbers)

for item in numbers:
    if item == num:
        print(True)
        isFind = True
if isFind == False:
    print(False)
