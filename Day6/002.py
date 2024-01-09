# collection 타입 : list, tuple, set, dictionary
# sequence 타입 : list, tuple

# list와 tuple의 차이점
# list는 mutable, tuple은 immutable

# 타입의 이름과 타입을 바꾸는 함수의 이름은 같다
list1 = [1, 3, 5]
tuple1 = tuple(list1)
list1 = list(tuple1)

# 데이터가 있다 -> Create Read Update Delete CRUD
list1.append(100)





print(list1)

# for 변수 in 컬렉션 :
for x in list1:
    pass
print(x)

# update
# index(리스트에서 값의 위치)로 update
list1[1] = 200
print(list1)

#delete
list1.remove(200)
print(list1)

del list1[2]
print(list1)
 