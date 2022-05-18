## 1. 문자 문제

'''
1-1. encode, decode
    문자의 단위 원소(코드 포인트)를 바이트로 변환하는 것을 인코딩, 바이트를 코드 포인트로 변환하는 것을 디코딩이라고 한다.
'''

string = '파이썬'
print(len(string))  # 3

byte = string.encode('utf8')    # 'utf-8' 아스키 코드와 호환되는 가장 흔한 8비트 인코딩 방식
print(byte) # b'\xed\x8c\x8c\xec\x9d\xb4\xec\x8d\xac'
print(len(byte))    # 9
print(byte.decode('utf8'))  # '파이썬'



'''
1-2. byte, bytearray
    불변형: byte
    가변형: bytearray
    str이 제공하는 대부분의 메서드 사용가능 (replace, startswith, strip, upper 등)
'''

## 2. 텍스트 파일 다루기

'''
2-1. 유니코드 샌드위치 (텍스트를 처리하는 최고의 방법) 165p
    1. 입력시 bytes를 디코딩 (bytes -> str)
    2. 텍스트를 오로지 str 객체로 다룬다. (100% str)
    3. 출력시 텍스트를 인코딩 (str -> bytes)
'''

f = open('python.txt', 'w', encoding='utf_8')
f.write('파이thon')
f.close()

f = open('python.txt', 'r', encoding='utf_8')   # encoding 지정하지 않으면 오류가 난다.
print(f.readline())


'''
2-2. 유니코드 정규화
    특히 발음기호가 있는 문자에서 unicodedata.normalize() 함수로 정규화를 통해 제대로 비교하기
'''


s1 = 'café'
s2 = 'cafe\u0301'
print('s1:',s1, 's2:', s2)
print("len(s1):", len(s1))  # 4
print("len(s2):", len(s2))  # 5
print("s1==s2", s1==s2) # False, 두 개의 시퀀스는 '규범적으로' 동일하지만, 파이썬은 동일하지 않다고 판단.

from unicodedata import normalize
normalized_s1 = normalize('NFC', s1)   # normalize 메서드의 첫번째 파라미터는 'NFC','NFD','NFKC','NFKD' 중 하나 (코드포인트 조합 방법을 의미)
normalized_s2 = normalize('NFC', s2)
print("len(normalized_s1):", len(normalized_s1))  # 4
print("len(normalized_s2):", len(normalized_s2))  # 5
print("normalized_s1==normalized_s2", normalized_s1==normalized_s2) # True
