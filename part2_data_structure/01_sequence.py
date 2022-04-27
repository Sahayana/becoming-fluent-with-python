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