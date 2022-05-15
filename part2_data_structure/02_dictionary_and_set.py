## 1. 일반적인 매핑형

'''
1-1 collections.abc
    dict 및 이와 유사한 자료형의 인터페이스를 정의하기 위해 Mapping 혹은 MutableMapping 클래스를 지원
'''

from collections.abc import Mapping
my_dict = {}
print('dict 자료형은 Mapping 클래스가 지원한다.', isinstance(my_dict, Mapping))  # True


'''
1-2 Dict 자료형 생성    
'''
dict1 = dict(one=1, two=2, three=3)
dict2 = {'one':1, 'two':2, 'three':3}
dict3 = dict(zip(['one','two','three'], [1,2,3]))
dict4 = dict([('two',2),('three',3),('one',1)])
dict5 = dict({'one':1, 'two':2, 'three':3})
print("dict1==dict2==dict3==dict4==dict5:", dict1==dict2==dict3==dict4==dict5)  # True


'''
1-3 지능형 딕셔너리 (Dict comprehension)    
'''

fruit_list = [('GRAPE', 5000), ('APPLE', 3000), ('ORANGE', 2000), ('BANANA', 4000)]
fruits_dict = {name.lower(): price for name, price in fruit_list}
print('fruits_dict:',fruits_dict)


'''
1-4 딕셔너리 자료형 조작
    https://dojang.io/mod/page/view.php?id=2307
'''


## 2. defaultdict과 __missing__()

'''
2-1 defaultdict
    존재하지 않는 key로 검색할 때 요청에 따라 항목을 생성하도록 설정
'''

my_dict = {'a':list()} # Not using defaultdict
iterwords = 'abcdefg'
try:
    for word in iterwords:
        my_dict[word].append(word)
except KeyError:
    pass

print(my_dict)

    
from collections import UserDict, defaultdict
my_dict = defaultdict(list) # default로 list 지정

for word in iterwords:
    my_dict[word].append(word)  # Key가 없어도 default로 설정한 list 객체를 생성하고 매핑한다.

print(my_dict)

'''
2-2 __missing()__
    기본 클래스인 dict에는 정의되어 있지 않다.
    dict 클래스를 상속하고 __missing__() 메서드를 정의하면 dict.__getitem__() 메서드가 key를 발견할 수 없을 때,
    KeyError를 발생시키지 않고 __missing__() 메서드를 호출
'''

class ListKeyDict(dict):    # defaultdict(list) 와 비슷한 커스텀 Dict 구현 by using __missing__() method
    def __missing__(self, key):
        self[key] = list()
        return self[key]

    def __contains__(self, key: object) -> bool:
        return key in self.keys() 

my_dict = ListKeyDict()
for word in iterwords:
    my_dict[word].append(word)
print('Dict 상속한 ListKeyDict:', my_dict)
print('a in my_dict:', 'a' in my_dict)


'''
2-3 UserDict 
    dict보다 UserDict을 상속하여 매핑형을 만드는 것이 쉽다.
    아무래도 내장 클래스를 바로 상속하여 오버라이딩하는 것은 까다롭다.
'''

class ListKeyDict(UserDict):    # defaultdict(list) 와 비슷한 커스텀 Dict 구현 by using __missing__() method
    def __missing__(self, key):
        self[key] = list()
        return self[key]
    
    def __contains__(self, key: object) -> bool:
        return key in self.data # UserDict은 dict을 상속하지 않고 내부에 실제 항목을 담고 있는 data라고 하는 dict객체를 가지고 있다.

my_dict = ListKeyDict()
for word in iterwords:
    my_dict[word].append(word)
print('UserDict 상속한 ListKeyDict:', my_dict)
print('a in my_dict:', 'a' in my_dict)