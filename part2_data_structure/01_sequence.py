## 1. 컨테이너 시퀀스와 균일 시퀀스

'''
1-1 Container Sequence
 서로 다른 자료형의 항목들을 담을 수 있다. (엄밀히 말해 객체에 대한 참조 reference count를 담고 있다.)
 List, Tuple, collections.deque 형
'''

'''
1-2 Flat Sequence
 단 하나의 자료형만 담을 수 있다. (객체에 대한 참조 대신 메모리 항목에 값을 직접 담는다. -> 담는 객체의 한계가 있지만 메모리를 더 적게 사용)
 str, bytes, bytearray, array.array 형
'''

## 2. 지능형 리스트 (List Comprehension)과 제너레이터 표현식

'''
2-1 지능형 리스트 (listcomp)는 오로지 새로운 리스트를 만드는 일만 한다.
 함수처럼 고유한 지역 범위를 가진다. 즉, 표현식 안에서 할당된 변수는 지역 변수
'''


fruits = 'pineapple apple peach pear banana'
fruits_list = [fruit.upper() for fruit in fruits.split() if len(fruit) > 5]
print(fruits_list)

'''
2-2 지능형 리스트와 map/filter 함수 비교
'''

fruits_list2 = list(filter(lambda fruit : len(fruit) > 5, map(lambda fruit : fruit.upper(), fruits.split()))) 
# filter 함수: filter(조건 함수, 순회 가능한 데이터) / map 함수: map(조건 함수, 적용시킬 데이터)
print(fruits_list2)

'''
2-3 데카르트 곱
'''

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

products = [(color, size) for color in colors for size in sizes]
print(products)

'''
2-4 제너레이터 표현식
 반복자 프로토콜을 이용하여 항목을 한번에 하나씩 생성, 리스트의 모든 항목을 메모리에 한번에 적재하지 않아 메모리 효율 좋음
 [] 대신 () 사용
'''

fruits_generator = (fruit.upper() for fruit in fruits.split() if len(fruit) > 5)
print(f'fruits_generator: {fruits_generator}')  # 제너레이터 오브젝트가 생성된다.
print(f'fruits_generator_tuple: {tuple(fruits_generator)}')

products_generator = (f'{color} {size}' for color in colors for size in sizes)
for product in products_generator:
    print('product: {}'.format(product))


## 3. 튜플은 단순한 불변 리스트가 아니다.

'''
3-1 레코드로 서의 튜플
 튜플의 각 항목은 레코드의 필드 하나를 의미하며 항목의 위치가 의미를 결정
'''

fruit, price = ('lemon', 5000)
print(fruit, price)

fruit_price_list = [(fruit, 5000) for fruit in fruits.split()]

for item in sorted(fruit_price_list):
    print('%s/%i' % item)

'''
3-2 튜플 언패킹
'''

for fruit, price in fruit_price_list:   # fruit, price를 병렬할당으로 언패킹
    print(fruit)

t = (20, 8)
quotient, remain = divmod(*t)   # *t 형식으로 언패킹
print(quotient, remain)

a,b,*rest = fruits.split()  # 초과 항목 처리
print(a,b,rest)


## 4. 슬라이싱

'''
4-1 슬라이스 및 범위 지정에서 마지막 항목이 포함되지 않는 이유
 길이 계산이 쉽다. ex) range(3) 은 3개의 항목(0,1,2)를 생성한다.
 특정 인덱스를 기준으로 겹침 없이 시퀀스 분할이 쉽다. ex) my_list[:x] / my_list[x:] 분할
'''

'''
4-2 슬라이스 객체
 mylist[a:b:c] 표기법은 인덱스 연산을 수행하는 [] 안에서만 가능하며 이는 slice(a, b, c) 객체를 생성한다.
 seq[start:stop:step] == seq.__getitem__(slice(start, stop, step))
'''

a_word = 'surrender'
print('a_word[::3]: ',a_word[::3])  # step = 3
print('a_word[::-1]: ',a_word[::-1])  # step이 음수일 경우 거꾸로 올라가면서 반환
print('a_word[::-3]: ',a_word[::-3]) 

# slice 객체 활용
a_sentence = 'Can we surrender'
head = slice(0, 4)
middle = slice(4, 7)
tail = slice(7, None)

print('head: ',a_sentence[head])
print('middle: ',a_sentence[middle])
print('tail: ',a_sentence[tail])

'''
4-3 슬라이스 생략 기호
 파이썬 생략기호 == (...), 슬라이스의 한 부분으로 전달 가능
 Numpy에서 자주 쓴다. ex) 4차원 배열 x에서 x[i, ...] == x[i, :, :, :,] 
'''

## 5. 시퀀스의 덧셈과 곱셈 연산자

'''
5-1 리스트의 리스트 만들기
 리스트를 초기화하는 경우 지능형 리스트를 사용하는 것이 좋다.
'''

# listcomp로 초기화
listcomp_board = [['_']*3 for i in range(3)]
listcomp_board[1][2] = 'X'
print(listcomp_board)    # board[1][2]의 요소만 바뀐다. [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]

# 곱셈 연산으로 초기화
multiple_board = [['_'] * 3] * 3
multiple_board[1][2] = 'X'
print(multiple_board)   # 내포된 리스트의 모든 [1][2]요소가 바뀐다. [['_', '_', 'X'], ['_', '_', 'X'], ['_', '_', 'X']]


## 6. 시퀀스의 복합 할당 (+= / *= 등)

'''
6-1 += / *= 등의 복합 할당 연산자는 피연산자에 따라 다르게 작동한다.
 += 연산자의 작동 메서드는 __iadd__이지만 미구현시, __add__ 메서드를 호출한다.
 a += b에서 a가 가변 시퀀스일때, __iadd__를 구현하면 a 값이 변경.
 그러나 __iadd__메서드가 없다면 a = a + b가 되어 a + b로 새롭게 생성된 객체가 a에 할당. 즉, __iadd__ 구현여부에 따라 객체의 정체성이 바뀐다.
 일반적으로 __iadd__를 구현하여 새로운 객체를 생성하는 것이 아닌 기존 객체의 값만 바꾸는 것이 좋다.
'''

# 가변 시퀀스에 복합 할당 적용하기

mutable_list = [1, 2, 3]
mutable_list_id = id(mutable_list)
print('mutable_list_id_before:', mutable_list_id)

mutable_list *= 2
print('mutable_list_id_after:', mutable_list_id)  # 메모리 id값이 같다.


# 불변 시퀀스에 복합 할당 적용하기

immutable_tuple = (1, 2, 3)
immutable_tuple_id = id(immutable_tuple)
print('immutable_tuple_id_before:', immutable_tuple_id)

immutable_tuple_id *= 2
print('immutable_tuple_id_after:', immutable_tuple_id)  # 메모리 id값이 다르다.



## 7. sort()와 sorted()


# sort()메서드는 사본을 만들지 않고 리스트 내부를 변경해서 정렬한다. (None 반환)
fruits = fruits.split()
print('original_fruits:', fruits)
print('fruits.sort():', fruits.sort())  # None 반환
print('sort()_fruits:', fruits) # 기존 리스트가 변경

# sorted()메서드는 새로운 리스트를 생성하여 반환한다.
money = [5000, 1000, 50000, 500]
print('sorted(money):', sorted(money))
print('sorted()_money:', money) # 기존 리스트는 변경 없음



## 8. 리스트가 답이 아닌 경우

'''
8-1 array
 리스트 안에 '숫자'만 들어있다면 배열(array.array)가 더 효율적이다.
 파이썬의 배열은 C 배열만큼 가볍고, 메모리 절약에 효과적이다.
 빠르게 파일을 저장하고 읽는 frombytes()나 tofile() 메서드도 추가로 제공한다.
'''
from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
fp = open('floats.bin', 'wb')
floats.tofile(fp)   # tofile(f): 이진 파일 f에 패킹된 기계값으로 항목 저장
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)     # fromfile(f, n): 패킹된 기계값으로 해석한 이진 파일 f에서 n개의 항목을 가져와 추가
fp.close()

print('floats==floats: ', floats==floats2) # True


'''
8-2 memoryview
 공유 메모리 시퀀스, bytes를 복사하지 않고 배열의 슬라이스를 다룬다. 
 배열등의 데이터 구조를 복사하지 않고 메모리를 공유할 수 있게 해준다.
'''
numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
memv_oct = memv.cast('B')
memv_oct.tolist()   # tolist(): 항목을 수치형 객체로 변환해서 넣은 리스트 반환, [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
memv_oct[5] = 4
print(numbers)  # array('h', [-2, -1, 1024, 1, 2])


'''
8-3 deque 및 기타 queue 
 덱 클래스는 큐의 양쪽 어디에서든 빠르게 삽입 및 삭제할 수 있도록 설계된 thread-safe 양방향 큐다.
 최대 길이를 설정해서 제한된 항목만 유지할 수도 있으며, 꽉 차게 되면 새로운 항목을 추가할 때 반대쪽 항목을 버린다.
'''

from collections import deque

dq = deque(range(10), maxlen=10)

dq.rotate(3)    # rotate(n): n 이 양수일경우 끝에서 n만큼 왼쪽 끝으로, 음수일경우 왼쪽 끝에서 n만큼 오른쪽 끝으로 이동
dq.appendleft(-1)   # appendleft(n): 가득찬 덱에 n 항목을 추가하면 반대쪽 항목 삭제
dq.extend([-5,-6,-7]) # extend(iter): iter인수에서 생성되는 항목을 덱의 오른쪽에 추가
dq.extendleft([100,200,300])    # extendleft(iter): iter인수에서 생성되는 항목을 덱의 왼쪽에 역순으로 추가
print(dq)
