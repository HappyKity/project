# 함수 만들기
def hello():
    print('hello world')

def python():
    print('python')

def massage():
    print('a')
    print('b')

#함수는 동시에 실해되지 않는다 (한번에 하나씩 실행)
# 병렬 프로그래밍 : 함수를 동시에 실행하는 것
massage()
print('c')
massage()