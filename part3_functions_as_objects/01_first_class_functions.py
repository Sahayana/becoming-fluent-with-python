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