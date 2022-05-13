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

