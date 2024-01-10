#for문

# hello를 for를 이용해 3번 출력하시오

for item in range(3):
    print('hello')

# for를 이용해서 0~10까지 출력
# for x in range(11):
#     print(x)

# for를 이용해서 0~10까지의 짝수 출력
for x in range(11):
    if x%2 == 0:
        print(x)

#1부터 5의 합계를 출력

num = 0
for item in range(1,6):
    num += item

print(num)

