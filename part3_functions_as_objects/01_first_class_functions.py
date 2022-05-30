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
from tkinter.messagebox import NO


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

'''
2-3 7가지 콜러블 객체
 - 사용자 정의 함수:    def or lambda
 - 내장 함수:           len(), time.strftime() 등의 built-in 함수
 - 내장 메서드:         dict.get() 등의 내장 메서드
 - 메서드:              클래스 본체에 정의된 함수
 - 클래스:              호출될 때 __new__() 메서드로 객체 생성 __init__()으로 초기화 (파이썬에는 new가 없으므로 클래스를 호출하면 객체생성)
 - 클래스 객체:         __call__() 메서드를 구현하면 이 클래스의 객체는 함수로 호출 될 수 있다.
 - 제너레이터 함수:     yield 키워드를 사용하는 함수나 메서드

 callable() 내장함수를 통해 호출 가능한 객체인지 판단 가능
'''

callable_list = [callable(obj) for obj in [abs, str, 1]]
print("callable_list: ",callable_list)  # [True, True, False]


'''
2-4 사용자 정의 콜러블형
 모든 파이썬 객체가 함수처럼 동작하게 만들려면 __call__() 메서드를 구현하면 된다.
'''

import random

class BingoCage:

    def __init__(self, items) -> None:
        self._items = list(items)   # items는 iterable한 객체를 받지만, 에러 방지를 위해 list로 한번 더 감싼다.
        random.shuffle(self._items) # 지역에 설정한 사본인 _items는 무조건 list이므로 shuffle실행에 부작용이 생기지 않는다.

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("Pick from empty BingoCage")
    
    def __call__(self):
        return self.pick()


bingo = BingoCage(list('abcdefg'))
print("bingo:", bingo)
print("bingo():", bingo())  # __call__() 
print("bingo.pick():", bingo.pick())
print("callable(bingo):", callable(bingo))  # True


'''
2-5 위치 매개변수와 키워드 매개변수
 함수를 정의할 때 키워드 전용 인수를 지정하려면 */** 가 붙은 인수 뒤에 이름을 지정한다.
'''

def html_tag(name, *contents, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(f' {key}="{value}"' for key, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if contents:
        return '\n'.join(f'<{name}{attr_str}>{content}</{name}>' for content in contents)
    else: return f'<{name}{attr_str} />'

print("html_tag('br'):",html_tag('br'))
print("html_tag('p', 'hello world!', id=1):",html_tag('p', 'hello world!', id=1))
book_data = {"name": "img", "title": "Fluent with Python", "src":"bookcover.png", "cls":"book_cover_img"}
print("html_tag(**book_data):",html_tag(**book_data))


'''
2-6 functools.partial()로 인수 고정하기
 functools.partial()은 함수를 부분적으로 실행할 수 있게 해주는 고위 함수다.
 어떤 함수에 partial()을 적용하면 함수의 일부 인수를 고정한 콜러블을 생성한다.
'''

from functools import partial
fixed_img_tag = partial(html_tag, name="img", cls="fixed_class_partial")
print("fixed_img_tag:",fixed_img_tag)    # functools.partial(<function html_tag at 0x0000025E0C4F5F70>, name='img', cls='fixed_class_partial')
print("fixed_img_tag.func:",fixed_img_tag.func) # <function html_tag at 0x000001B2090F4F70>
print("fixed_img_tag.args:",fixed_img_tag.args) # ()
print("fixed_img_tag.keywords:",fixed_img_tag.keywords) # {'name': 'img', 'cls': 'fixed_class_partial'}
print(fixed_img_tag(src="sunset.png"))