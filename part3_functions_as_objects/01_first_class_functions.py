## 1. 일급함수 (Firts-class functions)

'''
1-1 파이썬의 일급 객체
 - 런타임에 생성할 수 있다.
 - 데이터 구조체의 변수나 요소에 할당할 수 있다.
 - 함수 인수로 전달할 수 있다.
 - 함수 결과로 반환할 수 있다.
 
 함수뿐만이 아니라 정수, 문자열, 딕셔너리도 파이썬의 일급 객체다.
'''

'''
1-2 함수를 객체처럼 다루기
'''

def factorial(n:int) -> int:
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)

print("factorial(10):", factorial(10))
print("type(factorial):", type(factorial))  # function 클래스의 객체

fact = factorial    # 함수를 변수에 할당

fact_list = [fact(i) for i in range(0, 11)]
print("fact_list:", fact_list)


## 2. 고위 함수 (Higher-order fucntion)

'''
2-1 고위 함수
 함수를 인수로 받거나, 함수를 결과로 반환하는 함수
 map(), filter(), reduce() 등이 대표적
'''

fruits = ['apple', 'kiwi', 'orange', 'pineapple', 'strawberry', 'watermelon']

def reverse_key(word):  # sorted()의 key에 활용되는 함수는 인자를 하나만 받는다.
    return word[::-1]

print("sorted(fruits, key=reverse_key): ",sorted(fruits, key=reverse_key))  # ['orange', 'apple', 'pineapple', 'kiwi', 'watermelon', 'strawberry']
print("sorted(fruits, key=len): ",sorted(fruits, key=len))  # ['kiwi', 'apple', 'orange', 'pineapple', 'strawberry', 'watermelon']


'''
2-2 map(), filter(), reduce()의 대안
 함수를 인수로 받거나, 함수를 결과로 반환하는 함수
 map(), filter(), reduce() 등이 대표적
'''

# map과 filter의 대안 == 지능형 리스트
fact = factorial
list_for_map = list(map(fact, filter(lambda i : i % 2, range(1, 11))))
list_comp = [fact(i) for i in range(1,11) if i % 2]
print("list_for_map: ",list_for_map)
print("list_comp: ",list_comp)
print("list_for_map==list_comp:", list_for_map==list_comp)  # True

# reduce의 대안 == sum
from functools import reduce
from operator import add


val_reduce = reduce(add, range(100))
val_sum = sum(range(100))
print("val_reduce:", val_reduce)
print("val_sum:", val_sum)
print("val_reduce==val_sum:", val_reduce==val_sum)  # True

# all과 any

password = '123456789@'
condition = lambda x : x in '!@#%$^'
validation = [condition(word) for word in password] 
print('all(validation):', all(validation))  # False
print('any(validation):', any(validation))  # True

'''
2-2 익명 함수 lambda
 람다 구문은 단지 편리 구문(sugar syntax)이다.
 def와 마찬가지로 람다 표현식도 하나의 함수 객체를 생성하며, 여러 콜러블 객체중 하나이다.
 while, try 등의 파이썬 구문을 람다 본체에서 생성할 수 없다.
'''

print("sorted(fruits, key=lambda x : x[::-1]): ",sorted(fruits, key=lambda x : x[::-1]))    # ['orange', 'apple', 'pineapple', 'kiwi', 'watermelon', 'strawberry']